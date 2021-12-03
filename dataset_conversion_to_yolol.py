import os
import glob
import cv2
count=0
directory= "/home/suprim/dataset/Smartphone_sample_images/"
files= glob.glob(os.path.join(directory, "*.jpg")) 
for i in files:
    im = cv2.imread(i)
    print(im.shape)
    count +=1
print(count)