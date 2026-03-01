print("welcome to our home rent calculator")
from functools import reduce
room_rent=int(input("enter your total room rent : "))
snack_rent=int(input("enter your total snack rent :"))
know=input("are you know how much spent electric unit please say yes or no :")
if(know=="yes"):
    unit=float(input("enter your total spent electric unit :"))
    per_unit=float(input("enter your cost per one unit"))
    multi=unit*per_unit
elif(know=="no"):
    print("enter your total electric rent in other third party option")
    multi=0
list1=[]
other=input("have your spent money in your third party work please say yes or no")
if(other=="yes"):
    while("true"):
        other_rent=float(input("please enter other spent money"))
        list1.append(other_rent)
        others=input("next rent are you enter please yes or no")
        if(others=="no"):
            break

list1.append(multi)
list1.append(room_rent)
list1.append(snack_rent)
persons=int(input("how many persons living in room"))
total_money=reduce(lambda x,y:x+y,list1)
devide=total_money/persons
print(f"each person give {devide} rupees")
print("thanks for use me")




