class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m={}
        for i ,c in enumerate(numbers):
            m[c]=i
        for i in range(len(numbers)):
            new_target=target-numbers[i]
            if new_target in m and m[new_target]!=i :
                return [i+1,m[new_target]+1]
        return False