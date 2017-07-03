import os
from PIL import Image

pic_path = 'train_data/'
filelist = os.listdir(pic_path)
output = open('size_of_pic', 'w')

for filename in filelist:
    filepath = pic_path + filename
    try:
        im = Image.open(filepath)
        output.write(str(im.size[0]) + "," + str(im.size[1]) + "\n")
    except Exception, e:
        print Exception,":",e
output.close()

