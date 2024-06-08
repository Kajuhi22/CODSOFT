#Please Note that this is a simple calculator code without any exception handling

#def keyword is used to define a funstion
# ADDITION ARITHMETIC OPERATION

def add(z,x):
    return z+x

# Subtrction ARITHMETIC OPERATION

def subtract(z,x):
    return z-x

# Multiplication ARITHMETIC OPERATION

def multiply(z,x):
    return z*x

# Division ARITHMETIC OPERATION

def division(z,x):
    return z/x 

# Modular ARITHMETIC OPERATION

def modular(z,x):
    return z%x

# FloorDivision ARITHMETIC OPERATION

def floordivision(z,x):
    return z//x

# Exponent ARITHMETIC OPERATION

def exp(z,x):
    return z ** x


# def function main for looping
def main():
# Enter Input 1

    Input1 = float(input("Enter the input 'NUMBER 1' : "))

#Enter Input2

    Input2 = float(input("Enter the input 'NUMBER 2' : "  ))

#Enter the operator

    print("Enter the operation u want to perform from below:\n")

    print(" 1.Addition(+) \n 2.Subtraction(-)\n 3.Multiplication(*) \n 4.Division(/)")
    print(" 5.Modular(%) \n 6.Floor Division(//) \n 7. Exponential(**)")

#Select a number from above

    n=int(input("Enter number :"))

#Opertion Code

    if(n == 1):
        print(Input1 , " + ", Input2," = ",add(Input1,Input2))

    elif(n == 2):
        print(Input1 , " - ", Input2," = ",subtract(Input1,Input2))

    elif(n == 3):
        print(Input1 , " * ", Input2," = ",multiply(Input1,Input2))

    elif(n == 4):
        print(Input1 , " / ", Input2," = ",division(Input1,Input2))

    elif(n == 5):
        print(Input1 , " % ", Input2," = ",modular(Input1,Input2))

    elif(n == 6):
        print(Input1 , " // ", Input2," = ",floordivision(Input1,Input2))

    elif(n == 7):
        print(Input1 , " ** ", Input2," = ",exp(Input1,Input2))

    else:
        print("Invalid Input")
        print("MATH ERROR")
while True:
    main()
    run = input("Do you wnt to continue (y/n)?")
    if run == "n" :
        break
