from robot_control_class import RobotControl
import time

def limited_decimals(d):
    if(d>100):
        d=d
    else:
        a = int(d * 100)
        d = a/100
    return d

def get_laser(l,r):
    F = robocontrol.get_laser(359)
    F = limited_decimals(F)
    if (F<1.40):
        robocontrol.stop_robot()
    if(r==1):
        R1 = robocontrol.get_laser(150)
        R1 = limited_decimals(R1)
    elif(r==2):
        R2 = robocontrol.get_laser(0)
        R2 = limited_decimals(R)
    if(l==1):
        L1 = robocontrol.get_laser(600)
        L1 = limited_decimals(L1)
    elif(l==2):
        L2 = robocontrol.get_laser(719)
        L2 = limited_decimals(L)
    if(r==1):
        return L1,F,R1
    else:
        return L2,F,R2

x = time.time()
robocontrol = RobotControl()

  

while True:
    L,F,R = get_laser(1,1)
    print("L =",L,"F =",F,"R =",R)
    if(L<100 or F<100 or R<100):    
        if (((R<0.6 or L<0.6)and F>1.3)or (L<0.4 or R<0.4)):
            robocontrol.stop_robot()
            if (R<0.6):
                print("go left_forward")
                robocontrol.move_straight_time("backward",0.3,3)
                robocontrol.turn("counter-clockwise",0.3,0.5)  
                robocontrol.move_straight()
            elif (L<0.6):
                print("go right_forward") 
                robocontrol.move_straight_time("backward",0.3,3)
                robocontrol.turn("clockwise",0.3,0.5)          
                robocontrol.move_straight()
        elif F<1.30:
            robocontrol.stop_robot()
            L,F,R = get_laser(2,2)
            if(F<0.5):
                print("go backward_slowly")
                robocontrol.move_straight_time("backward",0.3,1)          
            elif (F<0.90):
                if (R>L):
                    print("Turn right")
                    robocontrol.turn("clockwise",0.3,5)  
                elif (R<L):
                    print("Turn left")
                    robocontrol.turn("counter-clockwise",0.3,5) 

            elif(F<1.30):    
                print("go forward_slowly")
                robocontrol.move_straight_time("forward",0.3,1)
        elif (F>0.90):
            print("go forward")
            robocontrol.move_straight()
    elif(L>100 and F>100 and R>100):
        robocontrol.stop_robot()
        y = time.time()
        your_time = y-x
        your_time = your_time/60
        your_time = limited_decimals(your_time)
        print(your_time , "min")    
        print("winner winnee diner diner")
        print("Thanks for watching")
        break 
