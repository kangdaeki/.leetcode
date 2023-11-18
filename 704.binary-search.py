class Solution:
    def bin_search(self, nums: List[int], target: int, lo:int, hi:int) -> int:
        if lo>hi: return -1
        mid=lo+(hi-lo)//2
        if nums[mid]==target: return mid
        elif nums[mid]<target: return self.bin_search(nums, target, mid+1, hi)
        else: return self.bin_search(nums, target, lo, mid-1)

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, target, 0, len(nums)-1)
