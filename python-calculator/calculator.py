"""
calculator

Description: calculator that can calculate

"""

from functions import check
from functions import multiply
from functions import divise
from functions import add
from functions import subtract
while(True):
    parts=[]
    answer="?"
    error=False
    print("Welcome to my calculator! use +,-,*,/ for operations.\nPlease use spaces between operators, type exit to end the program")
    print("What would you like to calculate?")
    equation=input()
    if equation =="exit":
        break
    parts=equation.split(" ")
    error=check(equation)
    for i in parts:
        if i.isdigit():
            i=float(i)
        elif isinstance(i, str):
            if i=="*":
                answer=multiply(answer, parts, i)
            elif i=="/":
                answer=divise(answer, parts, i)
    for i in parts:
        if i.isdigit():
            i=float(i)
        elif isinstance(i, str):
            if i=="-":
                answer=subtract(answer, parts, i)
            elif i=="+":
                answer=add(answer, parts, i)
    
    if error==False:
        print("Answer: "+str(answer)+"\n")
    else:
        print("\nERROR, Don't use letters\n")