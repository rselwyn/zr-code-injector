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

int main() {
  return 0;
}

API api;
Game game;