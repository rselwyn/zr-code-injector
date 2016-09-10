#!/usr/bin/python

from subprocess import call
import sys
import argparse

# Stand alone compiler executable

file_to_compile = sys.argv[1]
COMPILED_NAME = "COMPILED-" + file_to_compile

MAIN_FUNCTION = """

int main() {
  init();
  for (int i = 0; i <180; i++) loop();
  return 0;
}

"""

INJECT_SOURCE = """

#include <math.h>
#include <iostream>

/*
API class that represents the ZR Api functions.
*/
class API
{
   public:
      void setAttitudeTarget(float arr[3])
      {
         std::cout << "Setting attitude target: (" << arr[0] << " ," << arr[1] << " ," << arr[2] << ")" << std::endl;
      }

      void setPositionTarget(float arr[3]) {
        std::cout << "Setting position target: (" << arr[0] << " ," << arr[1] << " ," << arr[2] << ")" << std::endl;
      }

      void setVelocityTarget(float arr[3]) {
        std::cout << "Setting velocity target: (" << arr[0] << " ," << arr[1] << " ," << arr[2] << ")" << std::endl;
      }

      void setAttRateTarget(float arr[3]) {
        std::cout << "Setting attitude rate target: (" << arr[0] << " ," << arr[1] << " ," << arr[2] << ")" << std::endl;
      }

      void setForces(float forces[3]) {
        std::cout << "Setting forces: (" << forces[0] << " ," << forces[1] << " ," << forces[2] << ")" << std::endl;
      }

      void setTorques(float torques[3]) {
        std::cout << "Setting torque: (" << torques[0] << " ," << torques[1] << " ," << torques[2] << ")" << std::endl;  
      }

      void getMyZRState(float myState[12]) {
        std::cout << "Called getMyZRState" << std::endl;
      }

      void getOtherZRState(float otherState[12]) {
        std::cout << "Called getOtherZRState" << std::endl;
      }

      unsigned int getTime() {
        return 0;
      }
};

/**
Game specific functions
*/
class Game 
{
    public:
        bool dockItem() {
          return false;
        }

        void dropItem() {

        }

        int getNumItem() {
          return 0;
        }

        void getItemLoc(float pos[], int itemID) {

        }

        int hasItem(int itemId) {
          return 0;
        }

        int getItemType(int itemID) {
          return 0;
        }

        void dropSPS() {

        }

        float getScore() {
          return 0.0f;
        }

        float getOtherScore() {
          return 0.0f;
        }

        float getFuelRemaining() {
          return 0.0f;
        }

        int getCurrentTime() {
          return 0;
        }

        void sendMessage(unsigned char input) {

        }

        int getNumSPSHeld() {
          return 0.0f;
        }

        bool getZone(float zomeInfo[4]) {
          return false;
        }

        bool hasItemBeenPickedUp(int itemID) {
          return false;
        }
};

void DEBUG(std::string s) {
    std::cout << s << std::endl;
}

// ZR Math Function
float sqrtf(float x) {
  return sqrt(x);
}

float expf(float x) {
  return exp(x);
}

float log10f(float x) {
  return log10(x);
}

// Log rule
float logf(float x) {
  return log10(x)/log(exp(1));
}

void mathVecAdd(float *c, float *a, float *b, int n) {
  for (int i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
  }
}

float sinf(float x) {
  return sin(x);
}

float cosf(float x) {
  return cos(x);
}

float tanf(float x) {
  return tan(x);
}

float asinf(float x) {
  return asin(x);
}

float acosf(float x) {
  return acos(x);
}

float atanf(float x) {
  return atan(x);
}


float mathVecMagnitude(float *a, int n) {
  float sum = 0;
  for(int i = 0; i < n; i++) {
    sum += a[n] * a[n];
  }
  return pow(sum, 0.5);
}

float mathVecNormalize(float *a, int n) {
  float mag = mathVecMagnitude(a, n);
  for(int i = 0; i < n; i++) {
    a[n] /= mag;
  }
  return mag;
}

void mathVecSubtract(float *c, float *a, float *b, int n) {
  for (int i = 0; i < n; i++) {
    c[i] = a[i] - b[i];
  }
}


/*
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
NOTE:  EVERYTHING BELOW THIS LINE BESIDES THE INSTANTIATION
OF THE API AND GAME OBJECT WAS TAKEN FROM THE ZR MATH SOURCE CODE.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
*/

// Inverts a 3x3 matrix.  Returns false if successful
int mathInvert3x3(float inv[3][3], float mat[3][3]){
  float m11, m12, m13, m21, m22, m23, m31, m32, m33;
  float temp;
  
  m11 = mat[0][0];
  m12 = mat[0][1];
  m13 = mat[0][2];
  m21 = mat[1][0];
  m22 = mat[1][1];
  m23 = mat[1][2];
  m31 = mat[2][0];
  m32 = mat[2][1];
  m33 = mat[2][2];

  temp = m11*m22*m33 - m11*m23*m32 + m12*m23*m31 - m12*m21*m33 + m13*m21*m32 - m13*m22*m31;

  // must have non-zero determinant
  if (temp == 0.0)
    return 1;

  // make it multiplier to speed things up
  temp = 1/temp;

  inv[0][0] = temp*(m22*m33-m23*m32);
  inv[0][1] = temp*(m13*m32-m12*m33);
  inv[0][2] = temp*(m12*m23-m13*m22);
  inv[1][0] = temp*(m23*m31-m21*m33);
  inv[1][1] = temp*(m11*m33-m13*m31);
  inv[1][2] = temp*(m13*m21-m11*m23);
  inv[2][0] = temp*(m21*m32-m22*m31);
  inv[2][1] = temp*(m12*m31-m11*m32);
  inv[2][2] = temp*(m11*m22-m12*m21);

  return 0;
}

////////////////////////////////////////////////////////
// Produces the rotation matrix needed to transform a
// vector from the body frame specified by quat[] to the
// reference frame.  Assumes [vector scalar] quat representation
////////////////////////////////////////////////////////
void quat2matrixOut(float mat[3][3], float quat[4]){
  float q1 = quat[0], q2 = quat[1];
  float q3 = quat[2], q4 = quat[3];
  // make the rotation matrix from the quaternion
  mat[0][0] = q4*q4+q1*q1-q2*q2-q3*q3;
  mat[0][1] = 2*(q1*q2-q3*q4);
  mat[0][2] = 2*(q1*q3+q2*q4);
  mat[1][0] = 2*(q1*q2+q3*q4);
  mat[1][1] = q4*q4-q1*q1+q2*q2-q3*q3;
  mat[1][2] = 2*(q2*q3-q1*q4);
  mat[2][0] = 2*(q1*q3-q2*q4);
  mat[2][1] = 2*(q2*q3+q1*q4);
  mat[2][2] = q4*q4-q1*q1-q2*q2+q3*q3;
}

////////////////////////////////////////////////////////
// Produces the rotation matrix needed to transform a
// vector from the reference to the body frame specified
// by quat[].  Assumes [vector scalar] quat representation
////////////////////////////////////////////////////////
void quat2matrixIn(float mat[3][3], float quat[4]){
  float qInv[4];
  // invert the quaternion
  qInv[0] = -quat[0];
  qInv[1] = -quat[1];
  qInv[2] = -quat[2];
  qInv[3] =  quat[3];
  // inverse of Out is In
  quat2matrixOut(mat, qInv);
}  

////////////////////////////////////////////////////////
// Calculates the multiplication of quaternions q1 and q2
// q3 = q1*q2
////////////////////////////////////////////////////////
void quatMult(float *q3, float *q1, float *q2){
  // quaternion multiplication (successive rotation), q2 onto q1
  q3[0] = q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0];
  q3[1] = -q1[0]*q2[2] + q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1];
  q3[2] = q1[0]*q2[1] - q1[1]*q2[0] + q1[2]*q2[3] + q1[3]*q2[2];
  q3[3] = -q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] + q1[3]*q2[3];
  // normalize quaternion
  mathVecNormalize(q3,4);
}

////////////////////////////////////////////////////////
// Calculates the cross product of a and b
////////////////////////////////////////////////////////
void mathVecCross(float c[3], float a[3], float b[3]){
    c[0] = a[1]*b[2]-a[2]*b[1];
    c[1] = a[2]*b[0]-a[0]*b[2];
    c[2] = a[0]*b[1]-a[1]*b[0];
}


/*---------------------------------------------------------------------------------*/
void mathMatVecMult(float *c, float *a, float *b, int nr, int nc){
    int i,j,nci;
    for(i=0;i<nr;i++){
        c[i] = 0.0f;
        nci = nc*i;
        for(j=0;j<nc;j++){
            c[i] += a[nci+j]   *   b[j]; 
        }
    }
}

/*---------------------------------------------------------------------------------*/
void mathMatMatMult(float *c, float *a, float *b, int nra, int nca, int ncb){
    int i,j,k,ncbi,ncai;
    for(i=0;i<nra;i++){
      ncbi = ncb*i;
      ncai = nca*i;
        for(j=0;j<ncb;j++){
            c[ncbi+j]=0.0f;
            for(k=0;k<nca;k++){
                //  The i'th row and j'th column of c is:
                //  k'th entry in the i'th row of a  (TIMES)  k'th entry in the j'th column of b
                c[ncbi+j] += a[ncai+k] * b[k*ncb+j];
            }
        }
    }
}

/*---------------------------------------------------------------------------------*/
void mathMatMatTransposeMult(float *c, float *a, float *b, int nra, int nca, int nrb){
    int i,j,k,nrbi,ncai,ncaj;
    // For clarity, the number of columns in b must be the same as the number of columns in a for c = a*b'
    for(i=0;i<nra;i++){
      nrbi = nrb*i;
      ncai = nca*i;
        for(j=0;j<nrb;j++){
            ncaj = nca*j;
            c[nrbi+j] = 0.0f;
            for(k=0;k<nca;k++){
                //  c = a * b' where the rows of b' = columns of b etc...
                //  The i'th row and j'th column of c is:
                //  k'th entry in the i'th row of a  (TIMES)  k'th entry in the j'th row of b
                c[nrbi+j] += a[ncai+k] * b[ncaj+k];
            }
        }
    }
}

/*---------------------------------------------------------------------------------*/
void mathMatTransposeMatMult(float *c, float *a, float *b, int nra, int nca, int ncb){
    int i,j,k,ncbi;
    // For clarity, the number of rows in b must be the same as the number of rows in a for c = a'*b
    for(i=0;i<nca;i++){
      ncbi = ncb*i;
        for(j=0;j<ncb;j++){
            c[ncbi+j]=0.0f;
            for(k=0;k<nra;k++){
                //  c = a' * b where the rows of a' = columns of a etc...
                //  The i'th row and j'th column of c is:
                //  k'th entry in the i'th column of a  (TIMES)  k'th entry in the j'th column of b
                c[ncbi+j] += a[nca*k+i] * b[ncb*k+j];
            }
        }
    }
}

API api;
Game game;

"""

with open(COMPILED_NAME, "w") as to_compile:

	# Write the c++
	for i in INJECT_SOURCE.split('\n'):
		to_compile.write(i + '\n')

	# Write all the regular code
	with open(file_to_compile, "r") as in_file:
		for line in in_file:
			to_compile.write(line)

	for i in MAIN_FUNCTION.split('\n'):
		to_compile.write(i + '\n')

call(["g++", COMPILED_NAME, '-std=c++98', '-ferror-limit=100'])
call(["./a.out"])

# Short circuiting makes this work
if len(sys.argv) > 2 and sys.argv[2] == "clean":
	print "Cleaning"
	call(["rm", "a.out"])
	call(["rm", COMPILED_NAME])