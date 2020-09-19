class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenth = len(nums)
        for i in range(lenth):
            if(i+1<lenth):
                if nums[i]<nums[i+1]:continue
                else: return nums[i+1]
            else:return nums[0]