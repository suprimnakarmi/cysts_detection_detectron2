# import numpy as np
import json,os
import pandas as pd


image_directory ="/home/suprim/dataset/cysts_all/smartphone_standard/train"
df=pd.DataFrame(columns=["old_name", "new_name"])
df2=pd.DataFrame(columns=["no_image"])
old_name, new_name, no_image= [], [], [] # Used to 

# load the JSON file
json_file = os.path.join(image_directory, "via_final.json")   # Location for json file
img_count= 0

with open(json_file,"r") as f:  # Open a file handle for json file
    imgs_anno = json.load(f)

for idx,v in enumerate(imgs_anno.values()):  # Loop through all the values in the json file
  actual_file= v["filename"]
  filename=os.path.join(image_directory,actual_file)

  if os.path.isfile(filename):  # if file is present, then rename it
    new_file_name= "SR"+str(img_count).zfill(4)+".jpg"
    v["filename"]= new_file_name
    os.rename(f"{image_directory}/{actual_file}",f"{image_directory}/{new_file_name}")
    old_name.append(actual_file)
    new_name.append(new_file_name)
    img_count +=1

  else:   # Look if there are any missing file
    print(f"Image not found {filename}")
    no_image.append(actual_file)

with open("/home/suprim/dataset/cysts_all/smartphone_standard/train/new_json_file.json","w") as f:  # Create a file to dump the edited json file
  json.dump(imgs_anno,f)

# Save the file with old name, newname and no image in a separate excel file
dict_store = {'old_name': old_name, 'new_name': new_name}
dict_store2= {'no_image': no_image}

df=pd.DataFrame(dict_store)
df2=pd.DataFrame(dict_store2)

df.to_excel(r"/home/suprim/dataset/cysts_all/smartphone_standard/old_new_name.xlsx", index = False)
df2.to_excel(r"/home/suprim/dataset/cysts_all/smartphone_standard/no_image.xlsx", index = False)
