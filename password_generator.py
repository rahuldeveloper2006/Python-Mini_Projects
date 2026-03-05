#now i write a program to create random password
# i use random and string module
import random
import string

charecters=string.ascii_letters + string.digits + "#@!$#&~"
length=int(input("enter length of password you need : "))
password=""
for i in range(length):
    password=password+random.choice(charecters)

print(f"new strong password generated : {password}")