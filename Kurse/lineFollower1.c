#include <kipr/wombat.h>

int main()
{
    int lightSensor = 1, dark = 3900, light = 2500, targetLight = 3100, medium = (dark+light)/2, baseSpeed = 2500, dirCount = 0;
    float turnFaktor = 1.0;

    printf("setup\n");
    enable_servos();        

    while (1)
    {
        if ((dirCount<0 && analog(1)<targetLight) || (dirCount>0 && analog(1)>targetLight))
        {
            dirCount = 0;
        }
        else if(analog(1) < targetLight){
            dirCount++;
        }else{
            dirCount--;            
        }
        
        

        // printf("%i: %f\n", analog(1)-targetLight, 1 - (float)(analog(1)-targetLight)/750);
        turnFaktor = (float)(analog(1)-targetLight)/750;

        if(dirCount > 4 || dirCount < -4){
            mav(0, baseSpeed * (1-turnFaktor));
            mav(1, baseSpeed * turnFaktor);
        }else{
            mav(0, baseSpeed / 2);
            mav(1, baseSpeed / 2);
        }       

        msleep(1);
    }    

    return 0;
}