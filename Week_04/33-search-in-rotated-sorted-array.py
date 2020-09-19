class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while(lo<hi):
            mid = (lo+hi)//2
            if(nums[0]<=nums[mid] and (target>nums[mid] or target<nums[0])):
                lo=mid+1
            elif (target>nums[mid] and target < nums[0]):
                lo = mid +1
            else : hi = mid 
        return lo==hi and lo if nums[lo]==target else -1