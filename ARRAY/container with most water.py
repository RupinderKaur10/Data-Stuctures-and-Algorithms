heights = [1,2,1]
def mostWater(height):
    n = len(height)
    res = 0
    l,r = 0,n-1
    while l<r:
        area = (r - l) * (min(heights[l], heights[r]))
        res = max(area,res)
        if height[l]<heights[r]:
            l+=1
        else:
            r-=1
    return res
print(mostWater(heights))