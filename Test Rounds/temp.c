#include <kipr/wombat.h>

int main()
{
    void timed_servo_movement(port, position, time){
        /* Move the servo to a specific position in a specified total time in ms */
        int startPos = get_servo_position(port);
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
    
    
    printf("Hello World\n");
    int height=0, grapperHeight=1, grapperGrip = 2; 
    create_connect();
    enable_servos();

    camera_load_config("logs");
    camera_open();

    timed_servo_movement(height, 1800, 2000);
    set_servo_position(grapperHeight, 880);
    set_servo_position(grapperGrip, 2000);
    
    
    int count = get_object_count(0);
    int xPos = get_object_center_x(0, 0);
    int yPos = get_object_center_y(0, 0);
    int area = get_object_area(0, 0);
    
    /* while(1){
        camera_update();
        count = get_object_count(0);
        xPos = get_object_center_x(0, 0);
        yPos = get_object_center_y(0, 0);
        area = get_object_area(0, 0);
        printf("count: %i, xPos: %i, yPos: %i, area: %i\n", count, xPos, yPos, area);
    }*/

    return 0;
}