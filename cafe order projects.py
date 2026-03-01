import win32com.client
speaker=win32com.client.Dispatch("SAPI.spvoice")
print("arrey cafe")
name=input("enter your name: ")
name1=f"welcome  {name}  ,to our cafe. thanks for attain in our cafe"
food_list={
    "coffe":50,
    "tea":20,
    "blue coodrinks":160,
    "burger":200,
    "chicken tendudri":250,
    "cake":150,
    "ice-cream":50
}
speaker.speak(name1)
print("are you wants to give order")
speaker.speak(f"hello  {name}, are you wants to give order please say yes or no")
wish=input("enter yes or no : ")
count=0
list1=[]
if(wish=="yes"):
    speaker.speak(f"thank you  ,{name}  ,for agree to giev order, please select the food from list ")
    while "true":
     print("coffe:50\n tea:20 \n blue cooldrinks:160 \n burger:200 \n chicken tenduri:250 \n cake:150 \n ice-cream:50")
     speaker.speak("enter your item ")
     order1=input("enter your item : ")
     speaker.speak(f"wow , {name} ,you ordered {order1}")
     list1.append(order1)
     count=count+food_list[order1]
     print("your order has been conformed")
     speaker.speak("your order has been conformed")
     speaker.speak("are you want to order next item, please say yes or no")
     order2=input("are you want to order next item")
     if(order2=="no"):
        print("your total amount is",count)
        speaker.speak(f"thank you  ,{name} , you ordered , your total amount of items is {count}")
        break
     print(f"please wait {name} i will provide you all ordered items")
    speaker.speak(f"please wait {name} , i will provide all ordered items")
     


else:
    print("thanks for attain our cafe without order")
    speaker.speak(f"thanks {name} for attain our cafe without order")

print(f"your orders are {list1}")
speaker.speak(f"your orders are {list1}")
speaker.speak(f"extreamely thank you {name}")
