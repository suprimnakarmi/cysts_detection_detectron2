import numpy as np
import os,json,cv2,random


# Defined a function to create a dictionary in a format accepted by detectron2
def get_cysts_dicts(img_dir, split):
    # load the JSON file
    json_file = os.path.join(img_dir, "new_json_file.json")
    with open(json_file) as f:
        imgs_anns = json.load(f)

    dataset_dicts = []
    # loop through the entries in the JSON file
    for idx, v in enumerate(imgs_anns.values()):
        record = {}  # Initialize dict to add image name, image id and annotation in a format accepted by detectron2
        
        filename = os.path.join(img_dir, v["filename"])
        if os.path.isfile(filename):
          pass
        else:
          #print("Image not found", filename)
          continue
        
        record["file_name"] = filename
        annos = v["regions"]

        objs = []
        # one image can have multiple annotations, therefore this loop is needed
        for annotation in annos:
            # reformat the polygon information to fit the specifications
            anno = annotation["shape_attributes"]
            cx = anno["cx"]
            cy = anno["cy"]
            rx= anno["rx"]
            ry=anno["ry"]
            theta =anno["theta"]
            region_attributes = annotation["region_attributes"]["cyst"]
            # specify the category_id to match with the class.

            if "Giardia" in region_attributes:
                category_id = 1
            elif "Crypto" in region_attributes:
                category_id = 0
            

            obj = {
              
    
                #"segmentation": [poly],
    
                "category_id": category_id,
            }
            objs.append(obj)
        record["annotations"] = objs
        dataset_dicts.append(record)

        total_file = 830
        block = int(total_file/5)
        dataset_1 = dataset_dicts[0:block]
        dataset_2 = dataset_dicts[block:2*block]
        dataset_3 = dataset_dicts[2*block:3*block]
        dataset_4 = dataset_dicts[3*block:4*block]
        dataset_5 = dataset_dicts[4*block:5*block]
        #d = dataset_1 + dataset_2 + dataset_3 + dataset_4 
    print(total_file)
    print(block)
    print(len(dataset_1))
    print(len(dataset_2))
    print(len(dataset_3))
    print(len(dataset_4))
    print(len(dataset_5))
    if split == "train":
      return dataset_2 + dataset_3 + dataset_1 + dataset_4 + dataset_5
    if split == "val":
      return dataset_1


dataset_val = get_cysts_dicts("/home/suprim/dataset/cysts_all/smartphone_standard/train","val")

count_giardia =[]
count_crypto =[]
for r in dataset_val:
  image = r
  anno = r['annotations']   #all annotations of ground truth
  for a in range(len(anno)):
    if image['annotations'][a]['category_id'] == 0:
      count_crypto.append(0)
    else:
      count_giardia.append(1)
print(f"total_annotation_Giardia: {len(count_giardia)}")
print(f"total_annotation_Crypto: {len(count_crypto)}")
