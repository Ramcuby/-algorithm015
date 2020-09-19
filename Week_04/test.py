nums=[1,2,3,4,0]
def findMin(nums):
    lenth = len(nums)
    for i in range(lenth):
        if(i+1<lenth):
            if nums[i]<nums[i+1]:continue
            # elif i==lenth-1: return nums[0]
            else: return nums[i+1]
        else:return nums[0]
print(findMin(nums))
        