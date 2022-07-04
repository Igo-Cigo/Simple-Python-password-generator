import random
import string

print("If you want to save this password to an already existing file you need to move the file to the same directory as this python file and rename it to 'password.txt'")

# loops the input until the user provides a valid digit
while True:
    try:
        lenght = int(input("how long do you want your password to be? (Above 16 is recommended)\n"))
        if lenght > 0:
            break
    except ValueError:
        print("You must provide a valid digit greater than 0\n")

opt1 = input("Would you like to include symobls? (y/n)\n")
if opt1 == "y":
    symbols = string.punctuation
else:
    symbols = ""

opt2 = input("Would you like to include ASCII characters? (y/n)\n")
if opt2 == "y":
    include_ascii = string.ascii_letters
else:
    include_ascii = ""

opt3 = input("Would you like to include digits? (y/n)\n")
if opt3 == "y":
    digits = string.digits
else:
    digits = ""

if opt1 + opt2 + opt3 == "":
    print("Atleast one option must be specified for the program to continue")
    quit()

# Change the options by either using y or n which will change the structure of the passwrod
random = ''.join([random.choice(include_ascii + digits + symbols) for n in range(lenght)])
print("Your random passowrd is:", random)

# Ask the user if they wish to save their passwrod locally
save_password = input("Do you want to save your password? (y/n)\n")
usage = input("for what program do you want to save this password?\n").title()
if save_password == "y":
    file = open("password.txt", 'a')
    n = file.write("\n"+usage+": "+random)
    file.close()