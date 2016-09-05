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
        void takePic() {

        }

        int getEnergy() {
            return 0;
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

float mathVecNormalize(float *a, int n) {
  float mag = mathVecMagnitude(a, n);
  for(int i = 0; i < n; i++) {
  	a[n] /= mag;
  }
  return mag;
}

float mathVecMagnitude(float *a, int n) {
  float sum = 0;
  for(int i = 0; i < n; i++) {
  	sum += a[n] * a[n];
  }
  return pow(sum, 0.5);
}

void mathVecSubtract(float *c, float *a, float *b, int n) {
  for (int i = 0; i < n; i++) {
    c[i] = a[i] - b[i];
  }
}

API api;
Game game;
