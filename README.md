# 2D-Grid-Map
2023-summer-internship::2d grid map matching &amp; merging
자세한 내용은 노션페이지에 올려두었습니다. 
2d grid map merging notion page: https://www.notion.so/2D-GridMap-Matching-95c93fdd1a4d41cbbd01c7e79f8e6af0?pvs=4


---
### 0. roscore  실행

```
roscore
```
   
### 1. 새로운 terminal 창에 아래 명령들 실행
   
```
rosbag play <bag file>   
rosrun auto_merging int_to_np.py
```
/map 받아와서 행렬로 저장 (rosbag파일 필요)
위의 코드 진행 시, Occupancy grid map 아래 영상과 같이 변환

```
rosrun auto_merging priority.py
```
input map들을 비교하여 사이즈가 큰 맵부터 우선순위를 설정

```
rosrun auto_merging merge_with_np_optimization.py
```
위의 코드에서 받은 우선순위에 맞춰 순서대로 map 정합
