#Shaik Fahad
#Oct 08, 2024

name = input ("Hello, what's your name?")
print("Hello, " + name + " glad to meet you" + "!")
#This program greets with their name.

#2A:
authorized_names = ["fahad", "ben"]
name = input ("What is your name?")
if name in authorized_names:
    print ("Hello, "+ name  + " authroized!")
else:
    print("Unauthorized user.")
#This program allows only specfic users.