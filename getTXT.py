import os
import random

trainval_percent = 0.7      # 训练集和验证集 占 数据集 的比例
train_percent = 0.8         # 训练集 占 训练集和验证集 的比例
# 把xml路径修改为自己的Annotations文件夹路径
xml_path = '/home/zhang-jnqn/deep_learning/datasets/nanodet_voc_for_face_recognition/Annotations'
# 把保存路径修改为自己的Main文件夹路径
save_path = '/home/zhang-jnqn/deep_learning/datasets/nanodet_voc_for_face_recognition/ImageSets/Main'

total_xml = os.listdir(xml_path)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(save_path + '/trainval.txt', 'w')
ftest = open(save_path + '/test.txt', 'w')
ftrain = open(save_path + '/train.txt', 'w')
fval = open(save_path + '/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

