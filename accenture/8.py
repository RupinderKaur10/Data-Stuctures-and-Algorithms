def decToBase(n,num):
    notation = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",18:"I",19:"J",20:"K",21:"L",22:"M",23:"N",24:"O",25:"P",26:"Q",27:"R",28:"S",29:"T",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z"}
    res = []
    x = num%n
    if x<9:
        res.append(x)
    else: res.append(notation[x])
    q = num//n
    while q!=0:
        remainder = q%n
        if remainder<10:
            res.append(remainder)
        else: res.append(notation[remainder])
        q = q//n
    for i in range(len(res)-1,-1,-1):
        print(res[i],end="")
decToBase(21,5678)
# print(5/3)
