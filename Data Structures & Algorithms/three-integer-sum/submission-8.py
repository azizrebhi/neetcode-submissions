class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m={}
        l=[]
        for  i , k in enumerate(nums):
           m[k]=i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target=-nums[i]-nums[j]
                triplet = sorted([nums[i], nums[j], target])
                if target in m and m[target] > j and triplet not in l:
                    l.append(triplet) 
        return l