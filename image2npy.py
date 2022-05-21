from tkinter import W
import numpy as np
import imageio
import os
os.chdir('/home/zhang-jnqn/deep_learning/datasets/Lenet_for_face_recognition/test/')     #切换python工作路径到你要操作的图片文件夹，mri_2d_test为我的图片文件夹
a=np.ones((48,112,92,3))    #利用np.ones()函数生成一个三维数组，当然也可用np.zeros，此数组的每个元素a[i]保存一张图片
i=0
for filename in os.listdir(r"/home/zhang-jnqn/deep_learning/datasets/Lenet_for_face_recognition/test"):  #使用os.listdir()获取该文件夹下每一张图片的名字
	im=imageio.imread(filename)
	a[i]=im
	i=i+1
	if(i==48):   #190为文件夹中的图片数量
		break
np.save('/home/zhang-jnqn/deep_learning/datasets/Lenet_for_face_recognition/test_data.npy',a)
