#只需要修改self.src_path self.dst_path和i
#后缀部队的时候修改endswith 和 dst
#起始数字i
#由于直接保存在原路径下，就把dst注释掉了

import os

class BatchRename():
  '''
  批量重命名文件夹中的图片文件

  '''
  def __init__(self):
      self.src_path = '/home/zhang-jnqn/17_datasets/add_new/TV3'  # 表示需要命名处理的文件夹
      #self.dst_path = '/home/zhang-jnqn/17_datasets/add_new/chairdesk3'  # 表示处理后存放的文件夹

  def rename(self):
      filelist = os.listdir(self.src_path)  # 获取文件路径
      #print('filelist',filelist)

      total_num = len(filelist)  # 获取文件长度（个数）

      i = 6576  # 表示文件的命名是从1开始的

      for item in filelist:
          if item.endswith('.jpg'):  # 初始的图片的格式为jpg格式
              src = os.path.join(os.path.abspath(self.src_path), item)
          #dst = os.path.join(os.path.abspath(self.dst_path), format(str(i), '0>3s') + '.jpg')           
          dst = os.path.join(os.path.abspath(self.src_path), str(i) + '.jpg')   #这里之后要改回dst        
		#这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式
          try:
              os.rename(src, dst)
              #print('converting %s to %s ...' % (src, dst))
              i = i + 1
          except:
              continue
      print('total %d to rename' % total_num)


if __name__ == '__main__':
  demo = BatchRename()
  demo.rename()
