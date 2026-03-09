#now we wap to manage student grade
#Student Grade Management System

#now we make a empty dictionaty
database={

}
#now we make a function to add value and keys
def addStudent(name,value):
    database[name]=value
    print(f"the grade of {name} is {value} added sucessfully")

#now we define a function to update values

def updateValues(name,value):
    if name in database:
        database[name]=value
    else:
        print(f"{name} is not present so please enter valid name")

#now we define a function to delete items
def delete_item(name):
    if name in database:
        del database[name]
        print("data has been deleted sucessfully")
    else:
        print(f"{name} is not present so enter valid name")

#now we define a function to remove all data in database
def empty_data():
    for i in database.keys():
        del database[i]
    print("all data has been cleared successfully")

#now we define a method to view all key and values
def display():
    if database:
        for i in database.keys():
            print(f"{i} : {database[i]}")
    else:
        print("empty data present")

#now we define a method to display a specific data
def check_data(name):
    if name in database:
        print(f"{name} : {database[name]}")
    else:
        print("{name} is absent in database please enter valid name")

#now we write a choice method to perform a spesific operation

while(True):
    print("enter : \n1 for add data \n2 for update data \n3 for delete specific data \n4 for delete all data \n5 for display specific data \n6 for display all data in database \n7 for Exit")
    opt=int(input("select number : "))
    match(opt):
        case 1:
            name=input("enter student name : ")
            value=int(input("enter grade : "))
            addStudent(name,value)
        case 2:
            name=input("enter exists student name : ")
            value=int(input("enter new grade : "))
            updateValues(name,value)
        case 3:
            name=input("enter student name for delete : ")
            delete_item(name)
        case 4:
            empty_data()
        case 5:
            name=input("enter student name for check his/her grade : ")
            check_data(name)
        case 6:
            display()
        case 7:
            print("database system closed successfully")
            break
        case __:
            print("please enter valid number : ")
            




