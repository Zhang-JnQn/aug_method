from PIL import Image
import os
import random

imglist_name = []
imglist = []
bbxlist_name = []
#bbxlist = []


def get_img(inputpath):
    file_list = os.listdir(inputpath)
    last_path = inputpath
    for filename in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量
        # 否则每次只能遍历一层目录
        cur_path = os.path.join(inputpath, filename)
        if filename == "classes.txt":
            continue
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            last_path = cur_path
        elif os.path.splitext(filename)[1] == ".jpg":
            filename = os.path.join(last_path, filename)
            imglist_name.append(filename)
            imglist.append(Image.open(filename))
        elif os.path.splitext(filename)[1] == ".txt":
            filename = os.path.join(last_path, filename)
            bbxlist_name.append(filename)


def flip_data():

    for index in range(len(imglist)):
        img = imglist[index]
        # image翻转
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save(imglist_name[index].split(".jpg", 1)[0]+"_flipy.jpg")#保存在原位置

        file = open(bbxlist_name[index])

        for line in file.readlines():
            dataMat = []
            curLine = line.strip().split(" ")
            # 这里使用的是map函数直接把数据转化成为float类型
            floatLine = list(map(float, curLine))
            for i in range(4):
                dataMat.append(floatLine[1:][i])
            print("1",dataMat)
            newBBox = open(bbxlist_name[index].split(".txt", 1)[0]+"_flipy.txt", 'a')
            newBBox.write(str(int(floatLine[0])))
            # bbox翻转
            dataMat[1] = 1 - dataMat[1]
            print("2",dataMat)
            for data in dataMat:
                newBBox.write(' ')
                newBBox.write('%.6f' % (data))
            newBBox.write('\n')

if __name__ == "__main__":
    inputpath = "/home/zhang-jnqn/17_datasets/temp"
    get_img(inputpath)
    flip_data()
