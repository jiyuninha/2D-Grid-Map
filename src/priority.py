import os
import numpy as np
from queue import PriorityQueue
from merge_with_np_optimization import find_range

if __name__ == "__main__":
    # 파일 안에 있는 모든 np행렬 불러오기
    current_directory = "./output/floor6"
    file_list = os.listdir(current_directory)
    txt_files = [file for file in file_list if file.endswith('.txt')]
    que = PriorityQueue()

    for i, txt_file in enumerate(txt_files):
        file_path = os.path.join(current_directory, txt_file)
        numpy_arr = np.loadtxt(file_path,delimiter=", ")
        l_x, r_x, t_y, b_y = find_range(numpy_arr)
        width = r_x - l_x
        height = b_y - t_y
        data = (width * height, file_path)
        que.put(data)

    print(que.get())
    print(que.get())
    print(que.get())
    print(que.get())