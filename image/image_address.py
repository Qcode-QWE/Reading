import os
import sys
def get_image_address(file):
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))  # 获取项目根目录
    data_file_path = os.path.join(PROJECT_ROOT,file)  # 文件路径
    return data_file_path