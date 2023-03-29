#include <kipr/wombat.h>

int main()
{
    void timed_movement(port, position, time){
        /* Move the servo to a specific position in a specified total time in ms */
        int startPos = get_servo_position(port);
        if(startPos == position){
            int stepSize = 0;
            int stepTime = 0;
            while(stepTime == 0){
                stepSize++;
                stepTime = time / ((position-startPos)/stepSize);
            }
            int substepCount = (position-startPos) / stepSize;
            if(stepTime < 0){
                stepTime *= -1;
                substepCount *= -1;
            }
            printf("substepCount: %i; stepSize: %i; stepTime: %i; \n", substepCount, stepSize, stepTime);
            /* print(stepTime, stepSize, substepCount) */
            int i=0;
            while(i<=substepCount){
                /* print("move to: ", (startPos+stepSize*x), ", wait: ", stepTime) */
                /* printf("%i\n", (startPos + stepSize*i)); */
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
    }
    
    enable_servos();

    timed_movement(0, 100, 1000);
    
    disable_servos();
    
    return 1;
}
