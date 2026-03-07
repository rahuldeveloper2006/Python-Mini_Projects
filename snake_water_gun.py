#now we play snake water and game
import random
n=input("enter c for continue and s for stop")
while(n=="c"):
  computer=random.randint(0,2)
  number=int(input("enter 0 for snake,1 for water,2 for gun"))
  if(number>2 or number<0):
     print("please enter 0 to 2 number for play")
     break
  else:
   def check(computer,number):
     if(computer==number):
        return 0
     elif(computer==1 and number==2):
        return -1
     elif(computer==2 and number==0):
        return -1
     elif(computer==0 and number==1):
        return -1
     else:
        return 1
  print("choice of computer is: ",computer)
  print("choice of number is :",number)
  score=check(computer,number)
  if(score==0):
    print("match is draw")
  elif(score==-1):
    print("you get lost")
  elif(score==1):
    print("your are won")
  n=input("enter c for continue and s for stop")