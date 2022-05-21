import cv2
import os

xml_head = '''<annotation>
    <folder>17th_xunfei</folder>
    <!--文件名-->
    <filename>{}</filename>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>{}</width>
        <height>{}</height>
        <depth>{}</depth>
    </size>
    <segmented>0</segmented>
    '''

xml_obj = '''
    <object>        
        <name>{}</name>
        <pose>Rear</pose>
        <!--是否被裁减，0表示完整，1表示不完整-->
        <truncated>0</truncated>
        <!--是否容易识别，0表示容易，1表示困难-->
        <difficult>0</difficult>
        <!--bounding box的四个坐标-->
        <bndbox>
            <xmin>{}</xmin>
            <ymin>{}</ymin>
            <xmax>{}</xmax>
            <ymax>{}</ymax>
        </bndbox>
    </object>
    '''

xml_end = '''
</annotation>'''
 
labels = ['bed', 'chairdesk', 'food', 'person', 'pet', 'sofa', 'tableware', 'TV']#label for datasets
 
cnt = 0
txt_path=os.path.join('/home/zhang-jnqn/deep_learning/datasets/17th_for_nanodet/labels/val/')#yolo存放txt的文件目录
image_path=os.path.join('/home/zhang-jnqn/deep_learning/datasets/17th_for_nanodet/val/img/')#存放图片的文件目录
path=os.path.join('/home/zhang-jnqn/deep_learning/datasets/17th_for_nanodet/val/ann/')#存放生成xml的文件目录
 
 
for(root,dirname,files) in os.walk(image_path):#遍历图片文件夹
    for ft in files:
        ftxt=ft.replace('jpg','txt')#ft是图片名字+扩展名，将jpg和txt替换
        fxml=ft.replace('jpg','xml')
        fjpg = ft.replace('jpg', 'jpg')
        xml_path=path+fxml
        obj = ''
 
        img = cv2.imread(root+ft)
        img_h,img_w = img.shape[0],img.shape[1]
        head = xml_head.format(str(fjpg),str(img_w),str(img_h),3)
        
        with open(txt_path+ftxt,'r') as f:#读取对应txt文件内容
            for line in f.readlines():
                yolo_datas = line.strip().split(' ')
                label = int(float(yolo_datas[0].strip()))
                center_x = round(float(str(yolo_datas[1]).strip()) * img_w)
                center_y = round(float(str(yolo_datas[2]).strip()) * img_h)
                bbox_width = round(float(str(yolo_datas[3]).strip()) * img_w)
                bbox_height = round(float(str(yolo_datas[4]).strip()) * img_h)
 
                xmin = str(int(center_x - bbox_width / 2 ))
                ymin = str(int(center_y - bbox_height / 2))
                xmax = str(int(center_x + bbox_width / 2))
                ymax = str(int(center_y + bbox_height / 2))
 
                obj += xml_obj.format(labels[label],xmin,ymin,xmax,ymax)
        with open(xml_path,'w') as f_xml:
            f_xml.write(head+obj+xml_end)
        cnt += 1
        print(cnt)