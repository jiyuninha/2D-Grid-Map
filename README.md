# 2D-Grid-Map
2023-summer-internship::2d grid map matching &amp; merging


자세한 내용은 노션페이지에 올려두었습니다. 
2d grid map merging notion page: https://www.notion.so/2D-GridMap-Matching-95c93fdd1a4d41cbbd01c7e79f8e6af0?pvs=4


---
### cmd
   roscore
   
1. /map topic을 받아와서 numpy행렬로 저장 (rosbag파일 필요)
   
   rosbag play <bag file>
   
   rosrun auto_merging int_to_np.py
   
2. 정합
   
   rosrun auto_merging merge_with_np_optimization.py
   
3. 우선순위 확인
   
   rosrun auto_merging priority.py

...계속 수정 예정
