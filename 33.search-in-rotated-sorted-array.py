from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums: List[int], lo:int, hi:int) -> int:
            if lo>=hi: return lo
            if nums[lo]<nums[hi]: return lo
            mid=lo+(hi-lo)//2
            if nums[mid]<nums[lo]: return find_pivot(nums, lo, mid)
            else:  return find_pivot(nums, mid+1, hi)
        
        def bin_search(nums: List[int], target: int, lo:int, hi:int) -> int:
            if lo>hi: return -1
            mid=lo+(hi-lo)//2
            if target==nums[mid]: return mid
            elif target>nums[mid]: return bin_search(nums,target,mid+1,hi)
            else: return bin_search(nums,target,lo,mid-1)
        
        pivot_index=find_pivot(nums,0,len(nums)-1)
        if pivot_index==0: pivot_index=len(nums)
        if target==nums[0]: return 0
        elif target>nums[0]: return bin_search(nums,target,0,pivot_index-1)
        else: return bin_search(nums,target,pivot_index,len(nums)-1)
    