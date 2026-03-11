#Now we write a code to create a Advance File Management system
import os
import shutil
#now we define a function to view files
def view_files(path):
    files=os.listdir(path)
    print("\nFiles in directory : ")
    for file in files:
        print(file)

# now we define a function to create a file
def create_file(path):
    name=input("Enter name of the file : ")
    ful_path=os.path.join(path,name)
    with open(ful_path,"w") as f:
        f.write("New file is created")
    print("File is created successfully")

#now we define a function to delete a file
def delete_file(path):
    name=input("enter file name to delete : ")
    ful_path=os.path.join(path,name)
    if os.path.exists(ful_path):
        os.remove(ful_path)
        print("File deleted succesfully ")
    else:
        print("File not found")

#now we define a function to Rename a file
def file_rename(path):
    old_name=input("enter old file name : ")
    new_name=input("enter new file name : ")
    old_path=os.path.join(path,old_name)
    new_path=os.path.join(path,new_name)
    if os.path.exists(old_path):
        os.rename(old_path,new_path)
        print("file renamed successfully ")
    else:
        print("File not found")

#now we define a function to copy file
def copy_file(path):
    name=input("enter file name : ")
    destination=input("enter your destination path where you want to copy the file : ")
    ful_path=os.path.join(path,name)
    if os.path.exists(ful_path):
        shutil.copy(ful_path,destination)
        print("file copied successfully")
    else:
        print("File not found ")
    
#now we define a function to move the file 
def move_file(path):
    name=input("Enter file name : ")
    destination=input("Enter destination path to move the file : ")
    ful_path=os.path.join(path,name)
    if os.path.exists(ful_path):
        shutil.move(ful_path,destination)
        print("file moved successfully ")
    else:
        print("File not found ")

#now we define a function to find the folder size
def folder_size(path):
    total_size=0
    for root,dirs,files in os.walk(path):
        for file in files:
            ful_path=os.path.join(root,file)
            total_size=total_size+os.path.getsize(ful_path)
            print("Total folder size is : ",total_size)

def search_file(path):
    name=input("Enter file name to search : ")
    for root,dirs,files in os.walk(path):
        if name in files:
            print("File found at : ",os.path.join(root,name))
            return
    print("file not found ")

def main():
    path=input("Enter your folder path : ")
    while(True):
        print("\n======Advance file Manager ================")

        print("1. View Files")
        print("2. Create file")
        print("3. Delete file")
        print("4. Rename file")
        print("5. Copy file")
        print("6. Move file")
        print("7. Find Folder Size")
        print("8. Search file")
        print("9. Exit")
        choice=input("Enter your choice : ")
        if choice=="1":
            view_files(path)
        elif choice=="2":
            create_file(path)
        elif choice=="3":
            delete_file(path)
        elif(choice=="4"):
            file_rename(path)
        elif(choice=="5"):
            copy_file(path)
        elif(choice=="6"):
            move_file(path)
        elif(choice=="7"):
            folder_size(path)
        elif(choice=="8"):
            search_file(path)
        elif(choice=="9"):
            break
        else:
            print("invalid choice")

main()
