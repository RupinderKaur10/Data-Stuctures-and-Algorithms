def OperationChoices(c,a,b):
    if c ==1:
        return a+b
    elif c == 2:
        return a-b
    elif c==3:
        return a*b
    elif c ==4:
        return a/b
print(OperationChoices(2,16,20))