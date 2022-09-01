def NumberOfCarry(a,b):
    num1 = str(a)
    num2 = str(b)
    count = 0
    carry =0
    if len(num1)<=len(num2):
        l = len(num1)-1
    else: l = len(num2)-1
    for i in range(l+1):
        temp = int(num1[l-i])+int(num2[l-i])+carry
        if len(str(temp))>1:
            count+=1
            carry = 1
        else:
            carry = 0

    return carry+count
print(NumberOfCarry(451,349))
