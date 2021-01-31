import random
import pyperclip

password = ""
length = int(input("Length: "))

for i in range(0, length):
  password += chr(random.randint(33, 126))

print("Password: " + password)

if (input("Copy to clipboard (Y/N)? ")) in ["Y","y"]:
  pyperclip.copy(password)
