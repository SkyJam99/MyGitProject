from operations import *

#initialize variables
a, b, answer = 0, 0, 0
op = ""

#Tell user the operation choices and get user input here
print ("Available operations : +(sum), -(difference), *(multiply), /(divide)")

#Need to get int a and b, and String op (operation)

#Create if / elif / else statement for the different operations
if(op == "+"):
    answer = addition(a, b)
elif(op == "-"):
    answer = subtraction(a, b)
elif(op == "*"):
    answer = multiplication(a, b)
elif(op =="/"):
    answer = division(a, b)
else:
    print("Operation not recognized, please try again")


#Return the answer to the user in format (a "op" b = answer)
print (a, op, b,"=", answer)