import numpy as np
import cv2

def find_range(arr):
    x_l, x_r, y_t, y_b = 0, 0, 0, 0
    trans = arr.T
    reverse = arr[::-1]
    trans_r = np.flip(arr, axis=1).T

    x_l = np.argmax(np.any((trans == 0) | (trans == 10), axis=1))
    y_t = np.argmax(np.any((arr == 0) | (arr == 10), axis=1))
    y_b = 3999 - np.argmax(np.any((reverse == 0) | (reverse == 10), axis=1))
    x_r = 3999 - np.argmax(np.any((trans_r == 0) | (trans_r == 10), axis=1))
    return x_l, x_r, y_t, y_b

def compare_maps(map_arr,map_arr2):
    # map 크기 비교
    left_x1, right_x1, top_y1, bottom_y1 = find_range(map_arr)
    left_x2, right_x2, top_y2, bottom_y2 = find_range(map_arr2)
    w1 = right_x1 - left_x1
    h1 = bottom_y1 - top_y1
    w2 = right_x2 - left_x2
    h2 = bottom_y2 - top_y2
    l, r, t, b, m = 0, 0, 0, 0, 0

    if w1*h1 > w2*h2:
        # map_arr이 큰 경우
        l, r, t, b, m = left_x2, right_x2, top_y2, bottom_y2, 1
    else:
        # map_arr2가 큰 경우
        l, r, t, b, m = left_x1, right_x1, top_y1, bottom_y1, 2 
    return l, r, t, b, m


def transform_and_merge(map_arr, map_arr2):
    left, right, top, bottom, map = compare_maps(map_arr,map_arr2)
    large_map = np.zeros((4000,4000))
    small_map = np.zeros((4000,4000))
    img1 = cv2.imread('./map/floor3_map1.pgm',0)
    img2 = cv2.imread('./map/floor3_map2.pgm',0)
    mtrx = np.array([[-2.744547, 1.042311, 8090.697367],
                     [0.183950, -0.190427, 4808.119262],
                     [-0.000296, 0.000930, 1.000000]])
    if map == 1:
        # 크기가 큰 맵 선정 - transformed_map_arr
        large_map = np.copy(map_arr) # 2
        small_map = np.copy(map_arr2)
    else:
        large_map = np.copy(map_arr2) # 1
        small_map = np.copy(map_arr)

    for i in range(left, right + 1):
        for j in range(top, bottom + 1):
            original_pixel = np.array([i, j, 1])
            transformed_pixel = np.dot(mtrx, original_pixel)
            try:
                transformed_pixel_x = int(transformed_pixel[0] / transformed_pixel[2])
                transformed_pixel_y = int(transformed_pixel[1] / transformed_pixel[2])
            except OverflowError:
                continue

            if 0 <= transformed_pixel_x < 4000 and 0 <= transformed_pixel_y < 4000:
                if large_map[transformed_pixel_y][transformed_pixel_x] == -1:
                    large_map[transformed_pixel_y][transformed_pixel_x] = small_map[j - 1][i - 1]

    return large_map

if __name__ == "__main__":
    map_arr = np.loadtxt("./output/ouput_2.txt", delimiter=", ")
    map_arr2 = np.loadtxt("./output/ouput_1.txt", delimiter=", ")

    final_map = transform_and_merge(map_arr, map_arr2)
    np.savetxt("/home/dlwldbs/SPARO_tutorial/src/auto_merging/src/output/ouput_final.txt", final_map, delimiter=", ", fmt="%d")
