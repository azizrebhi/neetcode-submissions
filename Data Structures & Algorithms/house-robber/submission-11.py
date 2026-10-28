class Solution:
    def rob(self, nums: List[int]) -> int:
       cache = {}  # Created ONCE here, so all recursive calls can see it

       def dfs(current_nums):
            # Convert list to tuple so it can be used as a dictionary key
            state = tuple(current_nums)
            
            if state in cache:
                return cache[state]
            
            n = len(current_nums) - 1
            if n == -1: return 0
            if n == 0: return current_nums[0]
            if n == 1: return max(current_nums[0], current_nums[1])
            
            # Your exact recursive logic
            cache[state] = max(
                current_nums[n] + dfs(current_nums[0:n-1]),
                current_nums[n-1] + dfs(current_nums[0:n-2])
            )
            return cache[state]
            
       return dfs(nums)

          
           

          