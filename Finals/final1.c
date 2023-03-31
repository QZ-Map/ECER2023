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
        set_create_total_angle(0);
        while(get_object_center_x(object, 0) < 88 || get_object_center_x(object, 0) > 92 || get_object_area(object, 0) < 400 || get_object_count(object) < 1){
            if(get_create_total_angle()>150 || get_create_total_angle()<-150){
                create_disconnect();
                disable_servos();
            } 
            if(get_object_center_x(object, 0)<90 || get_object_area(object, 0)<400){           
                create_drive_direct(-20, 20);
                msleep(10);
            }else{          
                create_drive_direct(20, -20);
                msleep(10);
            }
            camera_update();
            printf("angle: %i\n", get_create_total_angle());
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
        msleep(200);
        create_drive_direct(0, 0);
    }

    int main()
    {
        int count, xPos, yPos, area;
        int height=0, grapperHeight=1, grapperGrip=2;
        int grapperClosed=800, grapperClosedLog=850, grapperOpen=1200;    
        int yellowLog = 0, botgal = 2;

        
        printf("setup\n");
        create_connect();
        enable_servos();
        
        set_create_distance(0);
        set_create_total_angle(0);
        
        timed_servo_movement(height, 0, 500);
        timed_servo_movement(grapperHeight, 300, 200);
        timed_servo_movement(grapperGrip, grapperClosed, 200);  
        
        wait_for_light(0);
        shut_down_in(118); 
        
        printf("start\n"); 

        create_drive_direct(200, 200);

        set_servo_position (height, 550);
        msleep(400);
        set_servo_position (grapperHeight, 920);
        
        create_drive_direct(200, -200);     //rotate to flip ring tower
        msleep(1500);    
        
        create_drive_direct(-200, 200);     //rotate back to the left
        msleep(1100);
        create_drive_direct(0, 0);

        
        create_drive_direct(200, 200);      //position for towers
        msleep(5500);
        create_drive_direct(0, 0);


        //!big tower 1
        camera_load_config("game");         //setup camera
        camera_open();
        printf("Tower 1\n");

        timed_servo_movement(height, 1800, 1000);       //prepare arm for botgal
        timed_servo_movement(grapperHeight, 750, 100);
        timed_servo_movement(grapperGrip, grapperOpen, 100);

        create_drive_direct(-200, 200);     //rotate to better position for tower detection
        msleep(400);
        create_drive_direct(0, 0);

        camera_update();
        //orient to center of cube
        camera_rotate_to_object(botgal);

        printf("get Botgal\n");

        //drive to botgal
        camera_drive_to_object(botgal);    

        timed_servo_movement(grapperGrip, grapperClosedLog, 500);   //pick up botgal
        timed_servo_movement(grapperHeight, 700, 200);
        timed_servo_movement(height, 2000, 500);
        timed_servo_movement(grapperHeight, 450, 200);

        /* printf("wait for other bot\n");
        msleep(2500);                  //long wait for other bot */

        create_drive_direct(-50, -50);         
        msleep(500);

        create_drive_direct(100, -100);         //rotate right
        msleep(3300);
        create_drive_direct(0, 0);

        printf("place Botgal\n");
        create_drive_direct(200, 200);          //place botgal
        msleep(1500);   
        create_drive_direct(0, 0);  
        timed_servo_movement(height, 400, 2000);
        timed_servo_movement(grapperHeight, 950, 500);
        timed_servo_movement(grapperGrip, grapperOpen, 200);
        timed_servo_movement(grapperHeight, 800, 200);

        timed_servo_movement(height, 1800, 1000);


        
        printf("Tower 2\n");
        create_drive_direct(-200, 200);         //rotate left and drive to second tower
        msleep(3000);
        create_drive_direct(200, 200); 
        msleep(1900);
        create_drive_direct(100, -100);       
        msleep(1700);
        create_drive_direct(0, 0);    


        //!big tower 2
        printf("Tower 2\n");

        timed_servo_movement(height, 1800, 1000);       //prepare arm for log pickup
        timed_servo_movement(grapperHeight, 800, 100);
        timed_servo_movement(grapperGrip, grapperOpen, 100);
        msleep(100);

        create_drive_direct(-200, 200);     //rotate to better position for tower detection
        msleep(100);
        create_drive_direct(0, 0);

        camera_update();

        //orient to center of cube    
        camera_rotate_to_object(yellowLog);

        printf("get Log 1\n");

        //drive to cube
        camera_drive_to_object(yellowLog);

        timed_servo_movement(grapperGrip, grapperClosedLog, 500);   //pick up log
        timed_servo_movement(height, 2000, 500);
        timed_servo_movement(grapperHeight, 200, 500);

        printf("wait for other bot\n");
        msleep(25000);                  //long wait for other bot

        create_drive_direct(-50, -50);          
        msleep(500);

        create_drive_direct(100, -100);         //rotate right
        msleep(2700);
        create_drive_direct(0, 0);

        printf("place Log 1\n");
        create_drive_direct(200, 200);          //place cube
        msleep(1600);   
        create_drive_direct(0, 0);  
        timed_servo_movement(height, 400, 2000);
        timed_servo_movement(grapperHeight, 950, 500);
        timed_servo_movement(grapperGrip, grapperOpen, 200);
        timed_servo_movement(grapperHeight, 800, 200);

        timed_servo_movement(height, 1800, 1000);


        
        printf("Tower 3\n");
        create_drive_direct(-100, 100);         //rotate left and drive to tower
        msleep(1500);
        create_drive_direct(200, 200); 
        msleep(3300);
        create_drive_direct(-100, 100);       
        msleep(800);
        create_drive_direct(0, 0);

        //!big tower 3
        //orient to center of cube    
        camera_rotate_to_object(yellowLog);

        printf("get Log 2\n");

        //drive to cube
        camera_drive_to_object(yellowLog);

        timed_servo_movement(grapperGrip, grapperClosedLog, 500);   //pick up log
        msleep(100);    
        timed_servo_movement(height, 2000, 500);
        timed_servo_movement(grapperHeight, 200, 500);

        printf("wait for other bot\n");
        msleep(1500);     //long wait for other bot

        create_drive_direct(-50, -50);
        msleep(500);

        create_drive_direct(100, -100);         //rotate right
        msleep(3500);
        create_drive_direct(0, 0);

        printf("place Log 2\n");
        create_drive_direct(200, 200);          //place cube
        msleep(1800);   
        create_drive_direct(0, 0);  
        timed_servo_movement(height, 400, 2000);
        timed_servo_movement(grapperHeight, 950, 500);
        timed_servo_movement(grapperGrip, grapperOpen, 200);
        timed_servo_movement(grapperHeight, 800, 200);

        timed_servo_movement(height, 1800, 1000);

        create_drive_direct(-200, -200);
        msleep(1500);
        create_drive_direct(0, 0);

        create_disconnect();

        return 0;
    }