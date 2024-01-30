#include <kipr/wombat.h>

int main()
{
    int lightSensor = 1, dark = 3900, light = 2500, targetLight = 3100, medium = (dark+light)/2, baseSpeed = 700, dirCount = 0, turnFaktor = 1;

    printf("setup\n");
    enable_servos();        

    while (1)
    {
        // turnFaktor = ((turnFaktor<0&&analog(1)>0.95*dark) || (turnFaktor>0&&analog(1)<1.05*light)) ? 0 : turnFaktor;
        /* if ((turnFaktor<0&&analog(1)>0.95*dark))
        {
            printf("1");
        }
        else if((turnFaktor>0&&analog(1)<1.05*light))
        {
            printf("2");
        } */
        
        turnFaktor += (analog(1)-targetLight-turnFaktor/10)/80;
        turnFaktor = (turnFaktor>baseSpeed ? baseSpeed : (turnFaktor<-baseSpeed ? -baseSpeed : turnFaktor));
        // printf("%d\n", turnFaktor);
        

        mav(0, baseSpeed - turnFaktor);
        mav(1, baseSpeed + turnFaktor);

        msleep(1);
    }    

    return 0;
}