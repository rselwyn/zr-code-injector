#include <math.h>

class API
{
   public:
      void setAttitudeTarget(float arr[3])
      {
         
      }

      void setPositionTarget(float arr[3]) {

      }

      void setVelocityTarget(float arr[3]) {

      }

      void setAttRateTarget(float arr[3]) {

      }

      void setForces(float forces[3]) {

      }

      void setTorques(float torques[3]) {

      }

      void getMyZRState(float myState[12]) {

      }

      void getOtherZRState(float otherState[12]) {

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

API api;
Game game;