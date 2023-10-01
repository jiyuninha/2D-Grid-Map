#!/usr/bin/env python3
import numpy as np
import rospy
from nav_msgs.msg import OccupancyGrid

total = None

def callback(data):
    global total 
    grid_data = data.data
    grid_width = data.info.width
    grid_height = data.info.height
    
    # data to np
    if total is None:
        total = np.array(grid_data).reshape((grid_height, grid_width))        
    else:
        grid_np = np.array(grid_data)
        b = np.where(grid_np==1, True, False).reshape((grid_height, grid_width)) # black pixel
        w = np.where(grid_np==0, True, False).reshape((grid_height, grid_width)) # white pixel
        total[np.logical_and(b, total == -1)] = 1
        total[np.logical_and(w, total == -1)] = 0

def listener():
    rospy.init_node('int_to_np', anonymous=True)
    global total 
    grid_width = 0
    grid_height = 0

    rospy.Subscriber('/map', OccupancyGrid, callback)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        if total is not None:
            np.savetxt("./output/floor6/floor6_1.txt", total[::-1], delimiter=", ", fmt="%d")
        rate.sleep()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
