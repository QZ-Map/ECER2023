void timed_movement(port, position, time){
    /* Move the servo to a specific position in a specified total time in ms */
    int startPos = get_servo_position(port);
    int stepSize = 0;
    int stepTime = 0;
    while(stepTime == 0){
        stepSize++;
        stepTime = time / ((position-startPos)/stepSize);
    }
    int substepCount = (position-startPos);    //stepSize
    /* print(stepTime, stepSize, substepCount) */
    int i=0;
    while(i<=substepCount){
        /* print("move to: ", (startPos+stepSize*x), ", wait: ", stepTime) */
        if(position>startPos){
            set_servo_position(port, (startPos + stepSize*i));
        }else{
            set_servo_position(port, (startPos - stepSize*i));
        }
        
        msleep(stepTime);
        i++;
    }
    /* print("move to: ", position) */
    set_servo_position(port, position);    
}

timed_movement(2, 1000, 1000);