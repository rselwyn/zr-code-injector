//Declare any variables shared between functions here

void init(){
    //This function is called once when your code is first loaded.

    //IMPORTANT: make sure to set any variables that need an initial value.
    //Do not assume variables will be set to 0 automatically!
}

void loop(){
    float pos[3] = {1.0,1.0, 1.0};
    api.setPositionTarget(pos);
}

