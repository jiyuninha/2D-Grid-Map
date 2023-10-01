import numpy as np
import cv2

gray = cv2.imread('./map/floor3_map1.pgm',cv2.IMREAD_GRAYSCALE)
print(gray.shape)
print(gray.shape[0])
print(type(gray.shape[0]))
arr = np.array((4000,4000))
for i in range(4000):
    for j in range(4000):
        arr[i][j] = gray[i][j]

np.savetxt("/home/dlwldbs/SPARO_tutorial/src/auto_merging/output/pgm_np.txt",arr,delimiter=", ",fmt="%d")
