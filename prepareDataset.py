import os
import shutil
import numpy as np
import tqdm
import sys
sys.path.append("C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5")

from cocoapi.PythonAPI.pycocotools.coco import COCO
data_source = COCO(annotation_file='C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5/TACO/data/annotations.json')

img_ids = data_source.getImgIds()

catIds = data_source.getCatIds()
categories = data_source.loadCats(catIds)
categories.sort(key=lambda x: x['id'])
classes = {}
coco_labels = {}
coco_labels_inverse = {}
for c in categories:
    coco_labels[len(classes)] = c['id']
    coco_labels_inverse[c['id']] = len(classes)
    # classes[c['name']] = len(classes)
    classes[len(classes)] = c['name']

class_num = {}

save_base_path  = 'C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5/tmp/labels/'
save_image_path = 'C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5/tmp/images/'

for index, img_id in tqdm.tqdm(enumerate(img_ids), desc='change .json file to .txt file'):
    img_info = data_source.loadImgs(img_id)[0]
    # 將含文件夾的路徑修改為文件名
    save_name = img_info['file_name'].replace('/', '_')

    # 移去文件擴展名
    file_name = save_name.split('.')[0]
    # 獲取單張圖像的寬和高
    height = img_info['height']
    width = img_info['width']
    # 轉換所得txt文件存儲路徑
    save_path = save_base_path + file_name + '.txt'

    is_exist = False  # 記錄圖片是否包含目標垃圾類型對象
    with open(save_path, mode='w') as fp:
        # 根據圖片編號找出垃圾對象的編號集合
        annotation_id = data_source.getAnnIds(img_id)
        boxes = np.zeros((0, 5))
        if len(annotation_id) == 0:  # 集合大小為0
            fp.write('')
            continue
        # 獲取coco格式的標籤
        annotations = data_source.loadAnns(annotation_id)
        lines = ''  # 記錄轉換後yolo格式的標籤
        # 遍歷對象標籤集
        for annotation in annotations:
            # 獲取垃圾對象的標籤
            label = coco_labels_inverse[annotation['category_id']]
            if label in classes.keys():
                # 垃圾類型屬於目標垃圾類型則進行格式轉換
                is_exist = True
                box = annotation['bbox']
                if box[2] < 1 or box[3] < 1:
                    # 如果原標籤中出現無長或寬數據的情況則跳過
                    continue
                # top_x,top_y,width,height==>cen_x,cen_y,width,height
                box[0] = round((box[0] + box[2] / 2) / width, 6)
                box[1] = round((box[1] + box[3] / 2) / height, 6)
                box[2] = round(box[2] / width, 6)
                box[3] = round(box[3] / height, 6)
                # label = classes[label]  # 標籤映射
                if label not in class_num.keys():
                    class_num[label] = 0
                class_num[label] += 1
                lines = lines + str(label)  # 先存儲標籤
                for i in box:  # 再存儲位置信息
                    lines += ' ' + str(i)
                lines += '\n'  # 換行
        fp.writelines(lines)

    if is_exist:
        # 存在目標類型對象，則拷貝圖像至指定目錄
        shutil.copy('C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5/TACO/data/{}'.format(img_info['file_name']), os.path.join(save_image_path, save_name))
    else:
        # 不存在則刪除所生成的標籤文件
        os.remove(save_path)

import splitfolders
splitfolders.ratio('C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5/tmp', output="C:/Users/default.DESKTOP-A0V01KV/PycharmProjects/detect_waste_yolov5/yolov5/taco", seed=1337, ratio=(.8, 0.1,0.1))














