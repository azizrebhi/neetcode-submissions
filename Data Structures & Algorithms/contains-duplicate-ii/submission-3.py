class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r=0
        s=set()
        for l in range(len(nums)):
            if l-r>k:
                s.remove(nums[r])
                r+=1
            if nums[l] in s :
                return True
            s.add(nums[l])
        return False
            