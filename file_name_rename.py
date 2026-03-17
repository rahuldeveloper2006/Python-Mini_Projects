#Now we write a python program to rename 100 files name with in 1sec

import os
folder_path=input("Enter your folder path : ")
files=os.listdir(folder_path)
for file_name in files:
    old_path=os.path.join(folder_path,file_name)
    #now check this is file or not
    if os.path.isfile(old_path):
        new_filename=file_name.replace(" ","_")
        new_path=os.path.join(folder_path,new_filename)
        #now we rename file in disk
        os.rename(old_path,new_path)
        print(f"Renamed : {file_name} ---> {new_filename}")
print("All files Renamed successfully !")