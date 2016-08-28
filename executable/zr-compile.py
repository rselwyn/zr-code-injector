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

void mathVecAdd(float *c, float *a, float *b, int n) {

}

float mathVecNormalize(float *a, int n) {
  return 0.0f;
}

float mathVecMagnitude(float *a, int n) {
  return 0.0f;
}

void mathVecSubtract(float *c, float *a, float *b, int n) {

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

call(["g++", COMPILED_NAME, '-ferror-limit=100'])
call(["./a.out"])

# Short circuiting makes this work
if len(sys.argv) > 2 and sys.argv[2] == "clean":
	print "Cleaning"
	call(["rm", "a.out"])
	call(["rm", COMPILED_NAME])