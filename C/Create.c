

// ^^^^^ temporary for functions that belong into an other file
// Driving vars
int fwd = 100;
int bwd = -100;
int turn = 100;
// Black line
int black = 2500;  
        


void driveStraight(speed_mm_s, distance_mm){
    /* speed in mm/sec, distance in mm
    | for backward driving speed negative, distance positive
    | should return isBumped in the future */    
    //print("driving straight for " + str(distance_mm) + "mm")
    int start_distance = RealDistance();
    if(speed_mm_s > 0){
        while((start_distance + distance_mm) > RealDistance()){
            create_drive_direct(speed_mm_s, speed_mm_s);
            msleep(1);
        }
    }else{
        while((start_distance - distance_mm) < RealDistance){
            create_drive_direct(speed_mm_s, speed_mm_s);
            msleep(1);
        }
    }
    create_drive_direct(0, 0);
}

void rotate(deg, speed){
    int start_distance = RealRotation();

    if(deg > 0){
        while(start_distance + deg > RealRotation()){
            create_drive_direct(-speed, speed);
            msleep(1);
        }
    }else{
        while(start_distance + deg < RealRotation()){
            create_drive_direct(speed, -speed);
            msleep(1);
        }
    }
    create_drive_direct(0, 0);
    msleep(2000);
}

void rotateAbsolute(deg){
    print("rotating absolute to " + str(deg));
    rotate(deg - RealRotation(), turn);
}