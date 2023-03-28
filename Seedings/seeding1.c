#include <kipr/wombat.h>

int main()
{
    printf("Hello World\n");
    int height=0, grapperHeight=1, grapperGrip = 2; 
    create_connect();
    enable_servos();

    
    set_servo_position (height, 0);
    set_servo_position (grapperHeight, 0);
    set_servo_position (grapperGrip, 1155);
    
    printf("setup\n");
	wait_for_light(1); 
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
    msleep(1600);
    
    
    create_drive_direct(-200, 200);
    msleep(1600);
    
    create_drive_direct(-200, -200);
    msleep(200);
    return 0;
}
