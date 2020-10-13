#! /usr/bin/env python

#attempt at making a library work that would read the keyboard
#failed because i kept getting an error from the library
#import keyboard 

print "db_keyboard"

import rospy
from std_msgs.msg import String 
import numpy as np

rospy.init_node('db_keypress')
pub = rospy.Publisher('/key_press', String, queue_size=1)


while(True):

    #if keyboard.is_pressed('W'):
    #    val = 'w'
    #else:

    val = raw_input("Input W/A/S/D: ")
    print(val)
    pub.publish(val)

