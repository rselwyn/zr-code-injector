#include <math.h>
#include <iostream>

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

int main() {
  return 0;
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