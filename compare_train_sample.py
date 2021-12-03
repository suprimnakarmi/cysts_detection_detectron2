import numpy as np
import pandas as pd
import albumentations as A 
import glob
import os
from tqdm import tqdm
import cv2
import random
from PIL import Image
from skimage import measure 
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

count=0
matched_images = []
images_path_train = '/home/suprim/dataset/smartphone_train_240'
id = 2
images_path_test = f"/home/suprim/dataset/samples_original_240/kalimati_summer/spinach/{id}"                                # Path to sample test images
image_files_train = glob.glob(os.path.join(images_path_train, "*.jpg"))     #List of all the train images
image_files_test = glob.glob(os.path.join(images_path_test, "*.jpg"))       # List of all the test images
df2 = pd.DataFrame(columns= ["sample_image", "train_file","sample"]) 
image_files_train = glob.glob(os.path.join(images_path_train, "*.jpg"))

for index,i in enumerate(tqdm(image_files_test)):    # Loop to test each test images with train images
  img_test = cv2.imread(i,0)

  for j in tqdm(image_files_train,position=0):
    img_train = cv2.imread(j,0)

    if img_test.shape != img_train.shape:   # If shape does not match, continue to next image 
      continue

    else:
      mse_e = mean_squared_error(img_test, img_train) 
      ssim_e = ssim(img_train, img_test, multichannel=True)

      eps=1e-6  
      if (mse_e<np.abs(eps)) and (ssim_e < (1+eps)) and (ssim_e> (1-eps)) : # Append the zipped file name in match images   
        matched_images.append((i, j))
        df2.loc[index, "train_file"] = j.split('/')[-1]
        df2.loc[index,"sample_image"] = i[41:]
        sample = 97
        df2.loc[index,"sample"] = sample
        print('\n')
        print(i,j)
        print('\n')
        count +=1
        break

print(f"\n Matched_count: {count}")
print(f"number of images in sample: {len(image_files_test)}")
df2.to_excel(rf"/home/suprim/dataset/excel_files/kalimati_summer/spinach/{id}.xlsx", index = False)
print(images_path_test)
print(f"sample ID: {sample}")