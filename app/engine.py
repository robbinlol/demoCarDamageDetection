#-----------------------------------------------------------------------#
#   predict.py将单张图片预测、摄像头检测、FPS测试和目录遍历检测等功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
#-----------------------------------------------------------------------#
import time
import os
import cv2
import numpy as np
from PIL import Image

from yolox.yolo import YOLO
from collections import Counter


def engine(img_path):
    yolo = YOLO()
    crop, count = False, False
    image = Image.open(img_path)
    r_image, labels = yolo.detect_image(image, crop=crop, count=count)
    file_name = img_path.split('/')[-1]

    print('FILE NAME')
    print(file_name)
    save_path = '../app/static/results/' + file_name

    r_image.save(save_path)
    print('SAVE PATH')
    print(save_path)

    # try:
    #     image = Image.open(img_path)
    # except:
    #     print('Open Error! Try again!')
    # else:
    #     r_image = yolo.detect_image(image, crop=crop, count=count)
    # r_image.show()
    # r_image.save("single_detect.jpg")
    labels = Counter(labels)
    return {
        'gate1': '进行车辆外观损伤识别： ',
        'gate1_result': 1,
        'gate1_message': {
            0: None,
            1: None
        },
        'gate2': 'Damage presence check: ',
        'gate2_result': 1,
        'gate2_message': {
            0: None,
            1: None
        },
        # 'location': 123,
        # 'severity': 456,
        'labels': labels,
        'final': '完成车辆外观损伤识别！'
    }
