"""
functions

Description: functions for the calculator
"""
def multiply(answer, parts, i):
    num1=parts.index(i)-1
    num2=parts.index(i)+1
    if answer=="?":
        answer+=float(parts[num1])*float(parts[num2])
        return answer
    else:
        answer*=float(parts[num2])
        return answer
    
def divise(answer, parts, i):
    num1=parts.index(i)-1
    num2=parts.index(i)+1
    if answer=="?":
        answer+=float(parts[num1])/float(parts[num2])
        return answer
    else:
        answer/=float(parts[num2])
        return answer
    
def add(answer, parts, i):
    num1=parts.index(i)-1
    num2=parts.index(i)+1
    if answer=="?":
        answer+=float(parts[num1])+float(parts[num2])
        return answer
    else:
        answer+=float(parts[num2])
        return answer
    
def subtract(answer, parts, i):
    num1=parts.index(i)-1
    num2=parts.index(i)+1
    if answer=="?":
        answer+=float(parts[num1])-float(parts[num2])
        return answer
    else:
        answer-=float(parts[num2])
        return answer
    
def check(e):
    for i in e:
        if i.isalpha():
            error=True
            return error
        else:
            error=False
            return error
        