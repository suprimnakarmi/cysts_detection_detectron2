import numpy as np
import pandas as pd
import albumentations as A 
import glob
import os
from tqdm import tqdm
import cv2
import random
from PIL import Image

images_path_train = '/home/suprim/dataset/brightfield_sample_pictures(jpg&png)' 
image_files_train = glob.glob(os.path.join(images_path_train, "*.png"))
for name in tqdm(image_files_train):
    file_name = name.split('/')[-1]
    img_train = cv2.imread(name)
    image = cv2.cvtColor(img_train, cv2.COLOR_BGR2RGB)
    transform = A.LongestMaxSize(max_size=240, interpolation=1, always_apply=False, p=1)
    random.seed(7)
    augmented_image = transform(image=image)['image']
    im = Image.fromarray(augmented_image)
    im.save(f"/home/suprim/dataset/brightfield_train_240/{file_name}","PNG")
print(images_path_train)