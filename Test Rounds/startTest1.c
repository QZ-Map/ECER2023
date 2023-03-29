#include <kipr/wombat.h>

void timed_servo_movement(port, position, time){
    /* Move the servo to a specific position in a specified total time in ms */
    int startPos = get_servo_position(port);
    if(startPos != position){
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

int main()
{
    printf("Hello World\n");
    int height=0, grapperHeight=1, grapperGrip = 2; 
    create_connect();
    enable_servos();

    
    timed_servo_movement(height, 0, 1000);
    set_servo_position (grapperHeight, 0);
    set_servo_position (grapperGrip, 1155);
    
    printf("setup\n");
    wait_for_light(0);
	shut_down_in(100);    
    
    printf("start\n");
    
    set_create_distance(0);
    set_create_total_angle(0);
    
    create_drive_direct(200, 200);
    msleep(10);

    set_servo_position (height, 300);
    msleep(1000);
    set_servo_position (grapperHeight, 850);
    
    create_drive_direct(200, -200);
    msleep(1500);
    
    
    create_drive_direct(-200, 200);
    msleep(1300);
    
    create_drive_direct(200, 200);
    msleep(1000);
    return 0;
}
