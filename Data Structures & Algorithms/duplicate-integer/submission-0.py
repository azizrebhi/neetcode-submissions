class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     S=set(nums)
     if len(S)==len(nums):
        return False
     else : 
        return True 