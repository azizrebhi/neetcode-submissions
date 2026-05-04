class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          indices={}
          for i in nums :
            indices[i] = indices.get(i, 0) + 1
        
          return [num for num, freq in sorted(indices.items(), key=lambda x: x[1], reverse=True)[:k]]

          
          