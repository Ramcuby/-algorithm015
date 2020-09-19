x=9
left,right = 0,x
        
while left <= right :
    mid = (left+right)//2
    # if x == 1:return 1
    if mid*mid == x:
        break
        # return int(mid)
    elif mid*mid < x:
        if((mid+1)*(mid+1)>x): break
        left = mid +1
    else:
        right = mid -1
print(mid)