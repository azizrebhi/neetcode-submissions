class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
           res=[]
           nums.sort()
           for i in range(len(nums)):
              l,r=i+1,len(nums)-1
              while l<r:
                 temp=nums[r]+nums[l]
                 if temp+nums[i]==0:
                    if [nums[r],nums[l],nums[i]] not in res : 
                      res.append([nums[r],nums[l],nums[i]])
                    l+=1
                    r-=1
                 elif temp+nums[i]>0:
                     r-=1
                 else :
                    l+=1
           return res

             
