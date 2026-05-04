class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        length=0 
        for i in range(len(nums)):
            if nums[i]==1 :
                length+=1
                if length>maxi:
                   maxi=length
            else :
                length=0 
        return maxi
