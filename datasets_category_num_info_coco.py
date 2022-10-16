import os
import json
import pandas as pd
from PIL import Image


def main(fmt):
    """

    :param fmt: 代表是coco格式还是voc格式
    :return: 返回一个csv文件，里面分别是图像的高度，宽度和数量
    """
    height = []
    width = []
    num = []
    cnt = {}
    if fmt == 'coco_format':

        #coco_root = './coco_instances_train2017.json'
        # vis_root = '../../code/mmdetection/data/coco/annotations/instances_train2017.json'
        ouc_root = './ouc_instances_train2017.json'
        with open(ouc_root, 'r') as f:
            json_file = json.load(f)
            # print(json_file['categories'])
            print("All labels: {}".format(len(json_file['annotations'])))
            # print(json_file['annotations'][0]['image_id'])
            for i in range(len(json_file['annotations'])):
                cat_id = json_file['annotations'][i]['category_id']
                if cat_id not in cnt:
                    cnt[cat_id] = 1
                else:
                    cnt[cat_id] += 1
    for key,val in cnt.items():
        print(key,val)




if __name__ == '__main__':
    fmt = "coco_format"  # or "voc_format"
    main(fmt)
