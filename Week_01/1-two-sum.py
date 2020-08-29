class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(0,lens):
            num = target - nums[i]
            if num in nums[i+1:]:
                j = i+nums[i+1:].index(num)+1
                break
        return [i,j]