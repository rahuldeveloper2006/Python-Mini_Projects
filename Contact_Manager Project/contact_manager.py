# now we write a program using python to make a contact manager app
# in this case we use JSON file
import json
file_name="contact_no.json"
def load_data():
    try:
        with open(file_name,"r") as f:
            data=json.load(f)
        return data
    except:
        return []

def save_data(data):
    with open(file_name,"w") as f:
        json.dump(data,f,indent=4)

#now we define a function to add contact number with name
def add_contact(name1,number1):
    data=load_data()
    adding_data={
        "Name":name1,
        "Contact_no":number1
    }
    data.append(adding_data)
    save_data(data)
    print("added contact successfully")

#now we define function to display all contacts
def display_all():
    data=load_data()
    try:
        if data:
            for contact in data:
                print(f"{contact["Name"]} : {contact["Contact_no"]}")
    except:
        print("Contacts Not Available")

#now we define a function to search specific
def search_contact():
    data=load_data()
    name=input("enter Contact name : ")
    found=False
    for i in data:
        if i["Name"]==name:
            print(f"{i["Name"]} : {i["Contact_no"]}")
            found=True
    if not found:
        print("Contact not found")
def delete_contact():
    new_data=[]
    found=False
    try:
        data=load_data()
        name=input("Enter Contact name : ")
        for i in data:
            if i["Name"]==name:
                found=True
            else:
                new_data.append(i)
        if found:
            save_data(new_data)
            print("contact deleted successfully")
        else:
            print("student not found")
    except:
        print("enter valid contact name")

#now we define a password checker to protect our contact manager
print("Welcome to our Contact Manager Machine")
password=642335
pas=int(input("enter your password : "))
if(pas==password):
    while(True):
        print("\n1. Add Contact_no")
        print("2. Display All Contact Number")
        print("3. Search Contact Number")
        print("4. Delete Contact Number")
        print("5. Exit")
        choice=int(input("enter your choice : "))
        if(choice==1):
            name=input("Enter Contact Name : ")
            number=input("Enter Contact Number : ")
            add_contact(name,number)
        elif(choice==2):
            display_all()
        elif(choice==3):
            search_contact()
        elif(choice==4):
            delete_contact()
        elif(choice==5):
            print("Thank you")
            break
        else:
            print("Invalid Choice")
else:
    print("Wrong password , Please try again later")
    exit()
