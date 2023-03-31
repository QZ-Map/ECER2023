    #include <kipr/wombat.h>

    void timed_servo_movement(port, position, time){
        /* Move the servo to a specific position in a specified total time in ms */
        int startPos = get_servo_position(port);
        if(startPos != position){
            int stepSize = 0;
            int stepTime = 0;
            while(stepTime == 0){
                stepSize++;
                stepTime = time /((position-startPos)/stepSize);
            }
            int substepCount =(position-startPos) / stepSize;
            if(stepTime < 0){
                stepTime *= -1;
                substepCount *= -1;
            }
            printf("substepCount: %i; stepSize: %i; stepTime: %i; \n", substepCount, stepSize, stepTime);
            int i=0;
            while(i<=substepCount){
                if(position>startPos){
                    set_servo_position(port,(startPos + stepSize*i));
                }else{
                    set_servo_position(port,(startPos - stepSize*i));
                }

                msleep(stepTime);
                i++;
            }
            set_servo_position(port, position);   
        } 
    }

    void camera_rotate_to_object(object){
        while(get_object_center_x(object, 0) < 88 || get_object_center_x(object, 0) > 92 || get_object_area(object, 0) < 400 || get_object_count(object) < 1){ 
            if(get_object_center_x(object, 0)<90 || get_object_area(object, 0)<400){           
                create_drive_direct(-20, 20);
                msleep(10);
            }else{          
                create_drive_direct(20, -20);
                msleep(10);
            }
            camera_update();
        }
    }

    void camera_drive_to_object(object){
        while(get_create_rbump() == 0 && get_create_lbump() == 0){  
            if(get_object_center_x(object, 0)<90){           
                create_drive_direct(80, 100);
                msleep(10);
            }else if(get_object_center_x(object, 0)>90){          
                create_drive_direct(100, 80);
                msleep(10);
            }else{
                create_drive_direct(100, 100);
                msleep(10);
            }
            camera_update();
        }
        create_drive_direct(-100, -100);
        msleep(100);
        create_drive_direct(0, 0);
    }

    int main()
    {
        printf("Hello World\n");

        int count, xPos, yPos, area;
        int height=0, grapperHeight=1, grapperGrip=2, grapperClosed=1100, grapperClosedLog=1150, grapperOpen=1550;    
        int yellowLog = 0, botgal = 2;

        
        printf("setup\n");
        create_connect();
        enable_servos();
        
        set_create_distance(0);
        set_create_total_angle(0);  
        
        //wait_for_light(0);
        shut_down_in(118); 
        
        printf("start\n");        


        //!big tower 1
        camera_load_config("game");         //setup camera
        camera_open();
        printf("Tower 1\n");

        printf("get Botgal\n");

        
        set_create_distance(0);
        create_drive_direct(50, -50);
        int i = 0;  
        while(i<10){
            printf("angle: %i\n", get_create_total_angle());
            i++;
            msleep(100); 
        }
        create_drive_direct(-50, 50);        
        set_create_distance(0);
        i = 0;         
        while(i<10){
            printf("angle: %i\n", get_create_total_angle());
            i++;
            msleep(100); 
        }
        create_drive_direct(0, 0);

        create_disconnect();

        return 0;
    }