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
    int count, xPos, yPos, area;


    printf("Hello World\n");
    int height=0, grapperHeight=1, grapperGrip=2, grapperClosed=1100, grapperClosedLog=1150, grapperOpen=1680;   
    create_connect();
    enable_servos();

    
    set_servo_position (height, 0);
    set_servo_position (grapperHeight, 0);
    set_servo_position (grapperGrip, 1155);
    
    printf("setup\n");
    //!wait_for_light(0);
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
    msleep(1400);
    create_drive_direct(0, 0);
    
    create_drive_direct(200, 200);
    msleep(2700);
    create_drive_direct(0, 0);

    

    //!tower code
    camera_load_config("game");
    camera_open();

    timed_servo_movement(height, 1800, 2000);
    set_servo_position(grapperHeight, 880);
    set_servo_position(grapperGrip, grapperOpen);
    msleep(100);

    create_drive_direct(-200, 200);
    msleep(200);
    create_drive_direct(0, 0);

    camera_update();
    printf("test_camera");

    //orient to center of cube
    while(get_object_center_x(0, 0) < 89 || get_object_center_x(0, 0) > 91 || get_object_area(0, 0) < 400 || get_object_count(0) < 1){ 
        if(get_object_center_x(0, 0)<90){           
            create_drive_direct(-20, 20);
            msleep(10);
        }else{          
            create_drive_direct(20, -20);
            msleep(10);
        }
        camera_update();
        count = get_object_count(0);
        xPos = get_object_center_x(0, 0);
        yPos = get_object_center_y(0, 0);
        area = get_object_area(0, 0);
        printf("count: %i, xPos: %i, yPos: %i, area: %i\n", count, xPos, yPos, area);
    }

    printf("\n\ndrive\n\n");

    //drive to cube
    while(get_create_rbump() == 0 && get_create_lbump() == 0){        //get_object_area(0, 0) < 2750
        if(get_object_center_x(0, 0)<90){           
            create_drive_direct(90, 100);
            msleep(10);
        }else if(get_object_center_x(0, 0)<90){          
            create_drive_direct(100, 90);
            msleep(10);
        }else{
            create_drive_direct(100, 100);
            msleep(10);
        }
        camera_update();

        count = get_object_count(0);
        xPos = get_object_center_x(0, 0);
        yPos = get_object_center_y(0, 0);
        area = get_object_area(0, 0);
        printf("count: %i, xPos: %i, yPos: %i, area: %i\n", count, xPos, yPos, area);
    }

    create_drive_direct(0, 0);

    timed_servo_movement(grapperGrip, grapperClosedLog, 500);
    msleep(100);    
    timed_servo_movement(height, 2000, 500);
    timed_servo_movement(grapperHeight, 200, 500);

    msleep(5000);     //long wait for other bot

    create_drive_direct(100, -100);         //rotate right
    msleep(2800);
    create_drive_direct(0, 0);

    create_drive_direct(200, 200);      //open grapper
    msleep(1000);     
    timed_servo_movement(height, 1800, 500);
    set_servo_position(grapperHeight, 880);
    set_servo_position(grapperGrip, grapperOpen);

    

    create_drive_direct(-100, 100);         //rotate left and drive to second tower
    msleep(1200);
    create_drive_direct(200, 200); 
    msleep(3000);
    create_drive_direct(-100, 100);       
    msleep(1000);
    create_drive_direct(0, 0);

    //!2. cube

    //orient to center of cube
    while(get_object_center_x(0, 0) < 89 || get_object_center_x(0, 0) > 91 || get_object_area(0, 0) < 400 || get_object_count(0) < 1){ 
        if(get_object_center_x(0, 0)<90){           
            create_drive_direct(-20, 20);
            msleep(10);
        }else{          
            create_drive_direct(20, -20);
            msleep(10);
        }
        camera_update();
        count = get_object_count(0);
        xPos = get_object_center_x(0, 0);
        yPos = get_object_center_y(0, 0);
        area = get_object_area(0, 0);
        //printf("count: %i, xPos: %i, yPos: %i, area: %i\n", count, xPos, yPos, area);
    }

    printf("\n\ndrive\n\n");

    //drive to cube
    while(get_create_rbump() == 0 && get_create_lbump() == 0){        //get_object_area(0, 0) < 2750
        if(get_object_center_x(0, 0)<90){           
            create_drive_direct(90, 100);
            msleep(10);
        }else if(get_object_center_x(0, 0)<90){          
            create_drive_direct(100, 90);
            msleep(10);
        }else{
            create_drive_direct(100, 100);
            msleep(10);
        }
        camera_update();

        count = get_object_count(0);
        xPos = get_object_center_x(0, 0);
        yPos = get_object_center_y(0, 0);
        area = get_object_area(0, 0);
        //printf("count: %i, xPos: %i, yPos: %i, area: %i\n", count, xPos, yPos, area);
    }

    
    msleep(1000);

    create_drive_direct(0, 0);

    timed_servo_movement(grapperGrip, grapperClosedLog, 500);
    msleep(100);    
    timed_servo_movement(height, 2000, 500);
    timed_servo_movement(grapperHeight, 200, 500);

    msleep(5000);     //long wait for other bot

    create_drive_direct(100, -100);         //rotate right
    msleep(3500);
    create_drive_direct(0, 0);

    create_drive_direct(200, 200); 
    msleep(1000);     
    timed_servo_movement(grapperGrip, grapperOpen, 500);

    create_disconnect();

    return 0;
}
