import os
import json
import pandas as pd
from PIL import Image

def main(fmt):

    height = []
    width = []
    num = []
    cnt = {}
    if fmt == 'coco_format':

        # coco_root = './coco_instances_train2017.json'
        # vis_root = '../../code/mmdetection/data/coco/annotations/instances_train2017.json'
        ouc_root = './ouc_instances_train2017.json'

        with open(ouc_root, 'r') as f:
            json_file = json.load(f)
            print(len(json_file['images']))
            for i in range(len(json_file['images'])):
                h = json_file['images'][i]['height']
                w = json_file['images'][i]['width']
                if (h, w) not in cnt:
                    cnt[(h, w)] = 1
                else:
                    cnt[(h, w)] += 1
    else:
        txt_path = r'C:\Users\wxd\Downloads\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\ImageSets\Main\train.txt'
        with open(txt_path, 'r') as f:
            for line in f.readlines():
                path = os.path.join(r"C:\Users\wxd\Downloads\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\JPEGImages",
                                    line.split("\n")[0] + ".jpg")
                img = Image.open(path)
                h, w = img.size
                if (h, w) not in cnt:
                    cnt[(h, w)] = 1
                else:
                    cnt[(h, w)] += 1

    for key, value in cnt.items():
        height.append(key[0])
        width.append(key[1])
        num.append(value)

    dataframe = pd.DataFrame({'height': height, 'width': width, 'num': num})
    dataframe.to_csv("ouc.csv", index=False, sep=',')




if __name__ == '__main__':

    fmt = "voc_format" # or "voc_format"
    main(fmt)
