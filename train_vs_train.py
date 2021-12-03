import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import os, json, cv2, random
import math
import glob
from tqdm import tqdm
print(np.__version__)
images_path_train = '/home/suprim/dataset/brightfield_train_240'
image_files_train_j= glob.glob(os.path.join(images_path_train, "*.jpg"))    #List of all the train images
image_files_train_p = glob.glob(os.path.join(images_path_train, "*.png"))   
image_files_train_1=image_files_train_p + image_files_train_j
image_files_train_2 = image_files_train_1
duplicate_1 = []
duplicate_2 = []
df = pd.DataFrame(columns= ["images", "duplicate"])
count=0
for i in tqdm(image_files_train_1):
    if i not in duplicate_2:
        for j in tqdm(image_files_train_2,position=0):
            if i == j:
                pass
            else:
                img1= cv2.imread(i)
                img2 = cv2.imread(j)
                img_shape1 = img1.shape
                img_shape2 = img2.shape
                if img_shape1 == img_shape2:
                    if (img1 == img2).all():
                        count +=1
                        print(i,j)
                        duplicate_1.append(i[43:])
                        duplicate_2.append(j[43:])
                        print(count)

dict_store = {'images': duplicate_1, 'duplicate': duplicate_2}
print(f"\n Matched_count: {count}")
df=pd.DataFrame(dict_store)
# print(f"number of images in sample: {len(image_files_test)}")
# print(images_path_test)
df.to_excel(r"/home/suprim/dataset/brightfield_train_vs_train.xlsx", index = False)

