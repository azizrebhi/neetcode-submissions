class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        postfix=[nums[len(nums)-1]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]*prefix[i-1])

            postfix.insert(0,nums[len(nums)-i-1]*postfix[len(postfix)-i])
        output=[postfix[1]]
        postfix.append(1)
        for i in range(1,len(nums)):
            target=prefix[i-1]*postfix[i+1]
            output.append(target)
        return output