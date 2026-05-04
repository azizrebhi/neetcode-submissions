class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r :
            if numbers[r]+numbers[l]==target :
                return [l+1,r+1]
            elif numbers[r]+numbers[l]<target:
                l=l+1
            else : 
                r=r-1
        