import os
count=0
directory = "/home/suprim/dataset/cysts_test/Suprim's prediction"

for dirname in sorted(os.listdir(directory)):  # List all the directories to access images under it.
    print(dirname)
    count +=1
    if os.path.isdir(f"{directory}/{dirname}"):   
        for filename in os.listdir(f"{directory}/{dirname}"):   # Loop through all the files under the file
            os.rename(f"{directory}/{dirname}/{filename}",f"{directory}/{dirname}/{count}_{filename}")   # Rename file using os.rename
