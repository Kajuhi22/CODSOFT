#import is udes to acces the random and string
#Random is used to randomize the password

import string
import random

#User Input
#Prompt the user to specify the desired length of the password

def Generator():
   length = int(input("Enter the password length : "))

#Generate Password
#Use a combination of random characters to generate a password of the specified length.


   print("choose a combination of random characters to generate a password of the specified length from below list :")
   print(" 1.Letters")
   print(" 2.Digits")
   print(" 3.Special characters")
   print(" 4.Exit")

   list=""
   while(True):
       
       pick = int (input("Pick a number from above options : "))
       if(pick == 1):
        # The ascii_letters are added to the password5
           list += string.ascii_letters

        # The digits are added

       elif(pick == 2):
           list += string.digits

           # The punctuation are added

       elif(pick == 3):
           list +=  string.punctuation

       elif(pick == 4):
           break
       
       else:
           print("Enter a valid number")

#Display the Password:
#Print the generated password on the screen.

   password = []
   for i in range(length):
      
      # choice is used to choose a list
      #random is used to get a random variable

      rand = random.choice(list)

      # the rand values are stores in password list

      password.append(rand)

      # The list values are joined together

   print(" The random password is "+ "".join(password))

while(True):
   Generator()

   run =input("Do you want to generate another pass word (y/n)? ")

   if(run == 'n'):
      break

