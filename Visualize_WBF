import os
import cv2
from PIL import Image

img_root = '../../data/datasets/VisDrone/VisDrone2019-DET-test-challenge/images/'
txt_root = '../../Visdrone-challenge/wbf_labels/'

for i in os.listdir(img_root):
    img_path = os.path.join(img_root,i)
    img = cv2.imread(img_path)
    txt_path = os.path.join(txt_root,i.replace('jpg','txt'))
    if not os.path.exists(txt_path):
        print(txt_path)
        continue
    with open(txt_path) as f:
        for line in f.readlines():

            #---------------------------------
            # yolo系列输出验证
            # line = line.strip().split(' ')
            # x = float(line[1])
            # y = float(line[2])
            # w = float(line[3])
            # h = float(line[4])
            #
            # x1 = x - (w / 2)
            # y1 = y - (h / 2)
            # x2 = x + (w / 2)
            # y2 = y + (h / 2)
            #
            # x1 = int(x1 * img.shape[1])
            # y1 = int(y1 * img.shape[0])
            # x2 = int(x2 * img.shape[1])
            # y2 = int(y2 * img.shape[0])
            #
            # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
            # cv2.putText(img, str(line[0]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            # cv2.imwrite("./img/"+i,img)  # 新建img,用来存储画框后的结果
            #-----------------------------

            line = line.strip().split(',')
            x = int(line[0])
            y = int(line[1])
            w = int(line[2])
            h = int(line[3])

            x1 = x
            y1 = y
            x2 = x + w
            y2 = y + h
            #
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv2.putText(img, line[5], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            cv2.imwrite("./img/"+i,img)  # 新建img,用来存储画框后的结果

