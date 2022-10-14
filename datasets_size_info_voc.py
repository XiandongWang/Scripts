import os
from PIL import Image
import pandas as pd
txt_path = r'C:\Users\wxd\Downloads\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\ImageSets\Main\train.txt'

height = []
width = []
num = []
cnt = {}
with open(txt_path, 'r') as f:
    for line in f.readlines():
        path = os.path.join(r"C:\Users\wxd\Downloads\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\JPEGImages", line.split("\n")[0]+".jpg")
        img = Image.open(path)
        h,w = img.size
        if (h, w) not in cnt:
            cnt[(h, w)] = 1
        else:
            cnt[(h, w)] += 1

for key,value in cnt.items():
    height.append(key[0])
    width.append(key[1])
    num.append(value)

dataframe = pd.DataFrame({'height':height,'width':width,'num':num})
dataframe.to_csv("voc.csv",index=False,sep=',')
