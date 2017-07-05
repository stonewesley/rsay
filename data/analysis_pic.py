import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

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
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,1,2)
ax1.hist(height, range = (0, 1600))
ax1.set_title('distribution of height')
ax2.hist(width, range = (0, 1200))
ax2.set_title("distribution of width")
a = np.array(height)
b = np.array(width)
a.dtype = "float64"
b.dtype = "float64"
c = a / b
ax3.hist(c, range = (0.5, 2))
ax3.set_title("distribution of ratio(height/width)")

plt.savefig('distribution_of_h_and_w.jpg')
