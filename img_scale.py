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

        cur_path = os.path.join(inputpath, filename)
        if filename == "classes.txt":
            continue
        if os.path.isdir(cur_path):
            last_path = cur_path
            # self.show_path_file(cur_path)
        elif os.path.splitext(filename)[1] == ".jpg":
            filename = os.path.join(last_path, filename)
            imglist_name.append(filename)
            # imglist.append(cv2.imread(filename))
            imglist.append(Image.open(filename))
        elif os.path.splitext(filename)[1] == ".txt":
            filename = os.path.join(last_path, filename)
            bbxlist_name.append(filename)
            # bbxlist.append()


def scale_data(scale):

    for index in range(len(imglist)):
        img = imglist[index]
        imx, imy = img.size
        bckgnd = Image.new('RGB', (imx, imy), (105+random.randint(-105, 150), 105+random.randint(-105, 150), 105+random.randint(-105, 150)))
        if (scale == 2):
            img = img.resize((imx//2, imy//2), Image.ANTIALIAS)
            bckgnd.paste(img, (0, 0))
            bckgnd.save(imglist_name[index].split(".jpg", 1)[0]+"_half.jpg")
        elif (scale == 4):
            img = img.resize((imx//4, imy//4), Image.ANTIALIAS)
            bckgnd.paste(img, (0, 0))
            bckgnd.save(imglist_name[index].split(".jpg", 1)[0]+"_quat.jpg")
        elif (scale == 8):
            img = img.resize((imx//8, imy//8), Image.ANTIALIAS)
            bckgnd.paste(img,(0,0))
            bckgnd.save(imglist_name[index].split(".jpg", 1)[0]+"_eigh.jpg")

        file = open(bbxlist_name[index])

        for line in file.readlines():
            dataMat = []
            curLine = line.strip().split(" ")
            # to float
            floatLine = list(map(float, curLine))
            for i in range(4):
                dataMat.append(floatLine[1:][i])
            print(dataMat)
            if (scale == 2):
                newBBox = open(bbxlist_name[index].split(".txt", 1)[0]+"_half.txt", 'a')
                newBBox.write(str(int(floatLine[0])))
                for data in dataMat:
                    data = data/2
                    newBBox.write(' ')
                    newBBox.write('%.6f' % (data))
                newBBox.write('\n')
            elif (scale == 4):
                newBBox = open(bbxlist_name[index].split(".txt", 1)[0]+"_quat.txt", 'a')
                newBBox.write(str(int(floatLine[0])))
                for data in dataMat:
                    data = data/4
                    newBBox.write(' ')
                    newBBox.write('%.6f' % (data))
                newBBox.write('\n')
            elif (scale == 8):
                newBBox = open(bbxlist_name[index].split(".txt", 1)[0]+"_eigh.txt", 'a')
                newBBox.write(str(int(floatLine[0])))
                for data in dataMat:
                    data = data/8
                    newBBox.write(' ')
                    newBBox.write('%.6f' % (data))
                newBBox.write('\n')


if __name__ == "__main__":
    inputpath = "/home/zhang-jnqn/Downloads/图片集/alljpg"
    scale = 2
    # 2  四分之一
    # 4  十六分之一
    # 8  六十四分之一
    get_img(inputpath)
    scale_data(scale)

