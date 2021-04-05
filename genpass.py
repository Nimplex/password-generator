from random import randint
from pyperclip import copy

password = ""

for i in range(0, int(input("Length: "))):
  password += chr(randint(33, 126))

print("Password: " + password)

if (input("Copy to clipboard (Y/N)? ")) in ["Y","y"]:
  copy(password)
