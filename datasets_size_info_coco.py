import os
import json
import pandas as pd
coco_root = './coco_instances_train2017.json'
vis_root = '../../code/mmdetection/data/coco/annotations/instances_train2017.json'
ouc_root = './ouc_instances_train2017.json'

height = []
width = []
num = []
cnt = {}

with open(ouc_root,'r') as f:
    json_file = json.load(f)
    print(len(json_file['images']))
    for i in range(len(json_file['images'])):
        h = json_file['images'][i]['height']
        w = json_file['images'][i]['width']
        if (h, w) not in cnt:
            cnt[(h, w)] = 1
        else:
            cnt[(h, w)] += 1

for key,value in cnt.items():
    height.append(key[0])
    width.append(key[1])
    num.append(value)

dataframe = pd.DataFrame({'height':height,'width':width,'num':num})
dataframe.to_csv("cnt_ouc.csv",index=False,sep=',')
