import os
import shutil
from tqdm import tqdm

SPLIT_PATH = r"D:\PycharmProject\xunlian\yolov5\my_data\GsMK_ImageSets\Main"
IMGS_PATH = r"D:\PycharmProject\xunlian\yolov5\my_data\images"
TXTS_PATH = r"D:\PycharmProject\xunlian\yolov5\my_data\labels"

TO_IMGS_PATH = r'D:\PycharmProject\xunlian\yolov5\my_data\GsMK_images'
TO_TXTS_PATH = r'D:\PycharmProject\xunlian\yolov5\my_data\GsMK_labels'

data_split = ['train.txt', 'val.txt','test.txt']
to_split = ['train', 'val','test']

for index, split in enumerate(data_split):
    split_path = os.path.join(SPLIT_PATH, split)

    to_imgs_path = os.path.join(TO_IMGS_PATH, to_split[index])
    if not os.path.exists(to_imgs_path):
        os.makedirs(to_imgs_path)

    to_txts_path = os.path.join(TO_TXTS_PATH, to_split[index])
    if not os.path.exists(to_txts_path):
        os.makedirs(to_txts_path)

    f = open(split_path, 'r')
    count = 1

    for line in tqdm(f.readlines(), desc="{} is copying".format(to_split[index])):
        # 复制图片
        src_img_path = os.path.join(IMGS_PATH, line.strip() + '.JPG')
        dst_img_path = os.path.join(to_imgs_path, line.strip() + '.JPG')
        if os.path.exists(src_img_path):
            shutil.copyfile(src_img_path, dst_img_path)
        else:
            print("error file: {}".format(src_img_path))

        # 复制txt标注文件
        src_txt_path = os.path.join(TXTS_PATH, line.strip() + '.txt')
        dst_txt_path = os.path.join(to_txts_path, line.strip() + '.txt')
        if os.path.exists(src_txt_path):
            shutil.copyfile(src_txt_path, dst_txt_path)
        else:
            print("error file: {}".format(src_txt_path))

