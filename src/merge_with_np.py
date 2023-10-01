#!/usr/bin/env python3
import numpy as np
import rospy
# from std_msgs.msg import String
# from nav_msgs.msg import OccupancyGrid
import cv2

def findRange(arr):
    # 배열에서 지도정보있는 영역 찾기
    # left_x 찾기 - trans배열에서 몇번째 row에 유효한 정보가 있는지 확인
    x_l, x_r, y_t, y_b = 0, 0, 0, 0
    trans = arr.T
    reverse = arr[::-1]
    trans_r = np.flip(arr,axis=1).T
    for i in range(4000):
        if np.any((trans[i] == 0) | (trans[i] == 10)):
            # 해당 row에 0이나 10인 값이 있을 경우, 그 row는 x_left값이 된다.
            x_l = i
            break
    for i in range(4000):
        if np.any((arr[i] == 0) | (arr[i] == 10)):
            y_t = i
            break
    for i in range(4000):
        if np.any((reverse[i] == 0) | (reverse[i] == 10)):
            y_b = 3999 - i
            break
    for i in range(4000):
        if np.any((trans_r[i] == 0) | (trans_r[i] == 10)):
            x_r = 3999 - i
            break
    
    return x_l, x_r, y_t, y_b

# 2 -> 1
map_arr = np.loadtxt("./output/ouput_1.txt", delimiter=", ")
map_arr2 = np.loadtxt("./output/ouput_2.txt", delimiter=", ")
mtrx = [[-2.744547, 1.042311, 8090.697367],
        [0.183950, -0.190427, 4808.119262],
        [-0.000296, 0.000930, 1.000000]]


# ouput_2에서 필요한 영역 추출
# trans_arr2 = map_arr2.T
# for i in trans_arr2:
#     if trans_arr2[i] in (10 or 0):

left_x, right_x, top_y, bottom_y = findRange(map_arr2)
print(left_x, right_x, top_y, bottom_y)

for i in range(left_x, right_x+1):
    for j in range(top_y, bottom_y+1):
        original_pixel = np.array([i, j, 1])
        transformed_pixel = np.dot(mtrx, original_pixel)
        try:
            transformed_pixel_x = int(transformed_pixel[0] / transformed_pixel[2])
            transformed_pixel_y = int(transformed_pixel[1] / transformed_pixel[2])
        except OverflowError:
            # 다음 픽셀로 넘어감
            continue

        # print((transformed_pixel_x,transformed_pixel_y))
        if transformed_pixel_x < 4000 and transformed_pixel_y < 4000:
            if map_arr[transformed_pixel_y][transformed_pixel_x] == -1:
                map_arr[transformed_pixel_y][transformed_pixel_x] = map_arr2[j-1][i-1] # map1에 맞는 행렬 위치 찾기

#print(trans[2000][2000])
np.savetxt("/home/dlwldbs/SPARO_tutorial/src/auto_merging/src/output/ouput_final.txt",map_arr,delimiter=", ",fmt="%d")

