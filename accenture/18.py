import math
x1,y1 = 1,1
x2,y2 = 2,4
x3,y3 = 3,6
res1 = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
res2 = math.sqrt(math.pow(x3-x2,2)+math.pow(y3-y2,2))
res3 = math.sqrt(math.pow(x3-x1,2)+math.pow(y3-y1,2))
print(round(res1),round(res2),round(res3))