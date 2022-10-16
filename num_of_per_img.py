import os
import pandas as pd

def main():
    """
    使用yolo格式的标注文件，可以方便快速的统计出每张图片有多少label
    :return: 每张图片的数量
    """
    cnt = {}
    ouc_root = '../../data/datasets/UAV-OUC-DET/labels/train2017/'
    vis_root = '../../data/datasets/VisDrone/VisDrone2019-DET-train/labels/'
    coco_root = './train2017/'
    for i in os.listdir(coco_root):
        txt_path = os.path.join(coco_root,i)
        with open(txt_path,'r') as f:
            num = len(f.readlines())
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
    a = [] # 每张图片含有多少个标注框
    b = [] # 含有相同标注框数量的图片有多少
    for k,v in cnt.items():
        a.append(k)
        b.append(v)
    dataframe = pd.DataFrame({'a': a, 'b': b})

    dataframe.to_csv("num_coco.csv", index=False, sep=',')


if __name__ == '__main__':
    main()
