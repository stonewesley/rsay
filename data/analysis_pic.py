import os
from PIL import Image
import matplotlib.pyplot as plt

pic_path = 'train_data/'
filelist = os.listdir(pic_path)
# output = open('size_of_pic', 'w')
height = []
width = []
for filename in filelist:
    filepath = pic_path + filename
    try:
        im = Image.open(filepath)
        height.append(im.size[0])
        width.append(im.size[1])
    except Exception, e:
        print Exception,":",e
# output.close()

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.hist(height)
ax1.set_title('distribution of height')
ax2.hist(width)
ax2.set_title("distribution of width")

plt.savefig('distribution_of_h_and_w.jpg')
