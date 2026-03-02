#now we make a project to check the enter password strong or not

import re
import win32com.client
speaker=win32com.client.Dispatch("SAPI.spvoice")

#at 1st we define a custom exception
class InvalidPasswordError(Exception):
    pass
def password_check(password):
    score=0
    if(len(password)>=8):
        score+=1
    else:
        speaker.speak("your password less than eight character so please enter password must be eight character")
        raise InvalidPasswordError("password should be at least 8 character long ")
    if(re.search(r"[A-Z]",password)):
        score+=1
    else:
        print("add at least one upper case")
    if(re.search(r"[a-z]",password)):
        score+=1
    else:
        print("add at least one lower case")
    if(re.search(r"[0-9]",password)):
        score+=1
    else:
        print("add atleast one number")
    if(re.search(r"[!@#$%^&*(),.?\":{}|<>]",password)):
        score+=1
    else:
        print("add at least one special character")

    print("\n password strength : ",end=" ")

    if(score==5):
        print("very strong password")
        speaker.speak(" excellent your password is very strong")
    elif(score>3):
        speaker.speak("mediam password")
        print("mediam strength password")
    else:
        speaker.speak("weak password")
        print("weak password")

password=input("enter your password : ")
password_check(password)