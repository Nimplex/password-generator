import random
import pyperclip
c=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]\\{|}~`")
p=""
l=int(input("Length: "))
i=0
while i<l:
 p+=c[random.randint(0,len(c)-1)]
 i+=1
print("Password: "+p)
if(input("Copy to clipboard (Y/N)? "))in["Y","y"]:
 pyperclip.copy(p)
