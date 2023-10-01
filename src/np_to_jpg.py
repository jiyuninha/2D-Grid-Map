import numpy as np
import cv2

# 예제 넘파이 배열
image_array = map_arr2 = np.loadtxt("./output/ouput_final.txt", delimiter=", ")

# 배열의 값 변환
image_array[image_array == -1] = 205
image_array[image_array == 10] = 0
image_array[image_array == 0] = 255

# 넘파이 배열을 그레이스케일 이미지로 변환
gray_image = image_array.astype(np.uint8)  # 데이터 타입을 uint8로 변환

# 그레이스케일 이미지를 파일로 저장
cv2.imwrite('gray_image_t3.pgm', gray_image)