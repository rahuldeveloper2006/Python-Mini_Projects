from datetime import datetime
from functools import reduce
import io
count=[]
i=0
def add_expense():
    total_amount=0
    amount=float(input("enter your expensi amount"))
    category=input("enter category")
    date=input("enter your date")
    total_amount=total_amount+amount
    if not date:
        date=datetime.today().strftime('%y-%m-%d')
    with open("store.txt","a")as f:
        f.write(f"date={date}   caregory={category}     amount={amount}   total amount={total_amount}\n")
        print("your amount add sucesfully")
def show_expense():
    with open("store.txt","r")as f:
        print(f.read())
def delete_expense():
    with open("store.txt","w")as f:
        f.truncate(0)
        print("deleted successfully")
def calculate_amount():
    print("please enter your amount 1 by 1")
    while("true"):
        condition=input("are you wants to calculate")
        if(condition=='yes'):
            size=int(input("enter how much number you want to calculate"))
            amount=0
            for i in range(1,size+1):
               am=int(input("enter amount"))
               amount=amount+am
            #     count.append(int(input("enter your amount")))
            # amount=reduce(lambda a,b:a+b,count)
            print(f"your total expence amounts are :{amount}")
        else:
            break

print("welcome to our expence management application")

def funct():
    if(cond=='yes'):
      print("1 for add expence\n2 for show expence\n3 for calculate your total expence\n4 for delete all expence")
      num=int(input("\nenter number betwen 1 and 4 :"))
      if(num==1):
       add_expense()
      elif(num==2):
       show_expense()
      elif(num==3):
        calculate_amount()
      elif(num==4):
         delete_expense()
     
while("true"):
   cond=input("are you wants to use the app : ")
   if(cond=='yes'):
      funct()
   else:
      break



