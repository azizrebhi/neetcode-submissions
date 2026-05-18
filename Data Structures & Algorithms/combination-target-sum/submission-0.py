class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curset,subsets=[],[]
        self.helper(0,curset,nums,subsets,target)
        return subsets

    def helper(self,i,curset,nums,subsets,target):
        if sum(curset)==target:
           subsets.append(curset.copy())
           return
        if i>=len(nums):
            return
        if sum(curset)>target:
            return 
        curset.append(nums[i])
        self.helper(i,curset,nums,subsets,target)
        curset.pop()
        self.helper(i+1,curset,nums,subsets,target)