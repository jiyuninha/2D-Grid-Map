import cv2
import numpy as np

# 이미지 불러오기
img1 = cv2.imread('./map_1.jpg')
img2 = cv2.imread('./map_one_1.jpg')

# gray scale 변환
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 특이점 찾기
detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(gray1, None) # 1에서의 특징점 검출
kp2, desc2 = detector.detectAndCompute(gray2, None) # 3에서의 특징점 검출

# 매칭
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches1 = matcher.match(desc1, desc2)

# 적절한 매칭점 선별
map1_pts = np.float32([kp1[m.queryIdx].pt for m in matches1])
map2_pts = np.float32([kp2[m.trainIdx].pt for m in matches1])

# RANSAC으로 호모그래피 변환 행렬 근사 계산
mtrx, mask = cv2.findHomography(map1_pts, map2_pts, cv2.RANSAC)
height, width, _ = img2.shape
aligned_img1 = cv2.warpPerspective(gray1, mtrx, (height, width))

# 컨투어로 지도영역만 추출
# contours, _ = cv2.findContours(aligned_img1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어로 지도영역만 추출
# draw1 = aligned_img1.copy()

# 컨투어 가져오기
# contours, _ = cv2.findContours(draw1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
# 컨투어 그리기
# draw_iamge = cv2.drawContours(draw1, contours, -1, (0,0,255), 5)
# 205인 빈 이미지 만들기


# cv2.imshow('d',draw_iamge)
# cv2.imwrite('./result/d1.jpg',draw_iamge)
# cv2.waitKey(0)

#cv2.imshow('d',cv2.resize(aligned_img1,(1000,1000)))
#cv2.waitKey()
#mtrx_inv = np.linalg.inv(mtrx)
for y_ in range(0, height-1):
    for x_ in range(0, width-1):
        #if aligned_img1[x_,y_] == 0:
            # 변환된 맵에 픽셀이 0인 값일 경우
        #pix = aligned_img1[x_,y_]
        #black_lower = 0
        #black_upper = 50
        #white_lower = 220
        #white_upper = 255

        #if pix < black_upper:
        #    img2[x_,y_] = pix
        #elif white_lower < pix:
        #    img2[x_,y_] = pix
        #else:

        #lower_w = (206,206,206)
        #upper_b = (50,50,50)
        #lower_b = (0,0,0)
        #if lower_w < (b,g,r) and upper_w > (b,g,r):
            #(x,y,z) = img2[x_,y_]
            #if (x,y,z) == (0,0,0):
            #    img2[x_,y_] = (205,205,205)
            #else:
            #if not (b,g,r):
            #    img2[x_,y_] = (205,205,205)
            #img2[x_,y_] = (b,g,r)
        #elif lower_b < (b,g,r) and upper_b > (b,g,r):
            #img2[x_,y_] = (b,g,r)
        if (b,g,r) != (205,205,205):
            img2[x_,y_] = (b,g,r)
#print('d')
# 관심영역 추출
# cv2.imshow('result',img2)
cv2.imwrite('./result/ppp.jpg',img2)
cv2.waitKey()
cv2.destroyAllWindows()

# transform matrix 찾기 mtrx의 역함수 찾기

# backward warping