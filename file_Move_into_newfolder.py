# Now we write a code to move all files in to another folder with in 1 sec

import os
import shutil
source_folder=input("Enter your Source path Where files are present : ")
name=input("Enter New Folder Name : ")
new_foldername=os.path.join(source_folder,name)
if not os.path.exists(new_foldername):
    os.makedirs(new_foldername)
files=os.listdir(source_folder)
for file in files:
    file_path=os.path.join(source_folder,file)
    if os.path.isfile(file_path):
        shutil.move(file_path,os.path.join(new_foldername,file))
print(f"All files move to {name} Folder Successfully")
