import os
import glob
from shutil import copyfile
# directory_ori_test = "/home/suprim/dataset/cysts_test/selected_test_images"
# directory_copy_test= "/home/suprim/dataset/cysts_test/Suprim's prediction"
# new_directory = "/home/suprim/dataset/cysts_test/selected_suprim_test"
directory_ori_test = "/home/suprim/dataset/Smartphone_sample_images"
directory_copy_test= "/home/suprim/dataset/Suprim_49"
new_directory = "/home/suprim/dataset/remaining_test"
selected_files =[]
other_files = []
files = glob.glob(os.path.join(directory_ori_test, "*.jpg")) 
files_to_copy = glob.glob(os.path.join(directory_copy_test, "*.jpg")) 
# print(files_to_copy[0][31:])

for i in files:
    selected_files.append(i[46:])

# for j in files_to_copy:
#     other_files.append(j[31:])
# print(len(selected_files))
# print(i[46:])
for dirname in sorted(os.listdir(directory_copy_test)):
    print(dirname)
    if os.path.isdir(f"{directory_copy_test}/{dirname}"):
        for filename in os.listdir(f"{directory_copy_test}/{dirname}"):
            if filename in selected_files:
            copyfile(f"{directory_copy_test}/{dirname}/{filename}",f"{new_directory}/{filename}")



# Uncomment for remaining test
# count = 0 
# for i in files:

#     if i[46:] in other_files:
#         copyfile(f"{directory_ori_test}/{i[46:]}",f"{new_directory}/{i[46:]}")
#         count+=1
#         print(i[46:])
# print(count)
