# turtle-bot_make-maze
This code can help you to make maze by turtle bot better and i test it on simulator in 
[robotigniteacademy](https://www.robotigniteacademy.com/en/course/python-3-for-robotics_38_0/).
## Algorithm
I used 2 function in this code which on of them can **getting laser** and the other can **limiting decimals**.

The algorithm of this code is such that ***three main conditions*** are used, which are as follows:
#### *1_ The robot takes a point of 45 degrees and 135 degrees and if it is less than 60 :*
* A_ If the distance of the robot at a point of 45 degrees is less than 60 cm, (the robot moves slightly backwards and turn left  and continues to move)
* B_ If the distance of the robot at a point of 135 degrees is less than 60 cm, (the robot moves slightly backwards and turn right and continues to move)
#### *2_ The robot takes a point of 90 degrees and if it is less than 1.30 cm :*
* A_ If the distance of robot at 90 degrees less then 50 cm, (the robot moves slightly backwards)
* B_ If the distance of robot at 90 degrees less than 90 cm, (the robot get 0 degrees and 180 degrees and then the robot rotates to a larger number)
* C_ If the distance of robot at 90 degrees greater than 90 cm (the robot moves slightly forwards)
#### *3_ If the above two conditions is false the robot will move forward*
