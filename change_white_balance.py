from PIL import Image
import cv2
import numpy as np
import os

imglist_name = []
imglist = []
bbxlist_name = []
kelvin_table = {
    1000: (255,56,0),
    1500: (255,109,0),
    2000: (255,137,18),
    2500: (255,161,72),
    3000: (255,180,107),
    3500: (255,196,137),
    4000: (255,209,163),
    4500: (255,219,186),
    # warm
    5000: (255,228,206),
    5500: (255,236,224),
    6000: (255,243,239),
    6500: (255,249,253),
    7000: (245,243,255),
    7500: (235,238,255),
    8000: (227,233,255),
    8500: (220,229,255),
    # cold
    9000: (214,225,255),
    9500: (208,222,255),
    10000: (204,219,255)}

def get_img(inputpath):
    file_list = os.listdir(inputpath)
    last_path = inputpath
    for filename in file_list:
        cur_path = os.path.join(inputpath, filename)
        if filename == "classes.txt":
            continue
        if os.path.isdir(cur_path):
            last_path = cur_path
        elif os.path.splitext(filename)[1] == ".jpg":
            filename = os.path.join(last_path, filename)
            imglist_name.append(filename)
            imglist.append(Image.open(filename))
        elif os.path.splitext(filename)[1] == ".txt":
            filename = os.path.join(last_path, filename)
            bbxlist_name.append(filename)


def convert_temp(image, temp):
    r, g, b = kelvin_table[temp]
    matrix = ( r / 255.0, 0.0, 0.0, 0.0,
               0.0, g / 255.0, 0.0, 0.0,
               0.0, 0.0, b / 255.0, 0.0 )
    return image.convert('RGB', matrix)

def change_white_balance(temp):
    for index in range(len(imglist)):
        img = imglist[index]
        # image翻转
        r, g, b = kelvin_table[temp]
        matrix = ( r / 255.0, 0.0, 0.0, 0.0,
                  0.0, g / 255.0, 0.0, 0.0,
                  0.0, 0.0, b / 255.0, 0.0 )
        img = img.convert('RGB', matrix)

        if temp == 9000:
          img.save(imglist_name[index].split(".jpg", 1)[0]+"_cold.jpg")#保存在原位置
        if temp == 5000:
          img.save(imglist_name[index].split(".jpg", 1)[0]+"_warm.jpg")#保存在原位置



        file = open(bbxlist_name[index])

        for line in file.readlines():
            dataMat = []
            curLine = line.strip().split(" ")
            # 这里使用的是map函数直接把数据转化成为float类型
            floatLine = list(map(float, curLine))
            for i in range(4):
                dataMat.append(floatLine[1:][i])
            print(dataMat)
            if temp == 9000:
              newBBox = open(bbxlist_name[index].split(".txt", 1)[0]+"_cold.txt", 'a')
            if temp == 5000:
              newBBox = open(bbxlist_name[index].split(".txt", 1)[0]+"_warm.txt", 'a')
            newBBox.write(str(int(floatLine[0])))
            # bbox翻转
            for data in dataMat:
                newBBox.write(' ')
                newBBox.write('%.6f' % (data))
            newBBox.write('\n')

if __name__ == "__main__":
    inputpath = "/home/zhang-jnqn/17_datasets/temp"
    get_img(inputpath)
    change_white_balance(9000)
    # 9000 warm
    # 5000 cold
