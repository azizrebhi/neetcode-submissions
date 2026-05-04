class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = defaultdict(list) 
        
        for word in strs:
            key = tuple(sorted(word))  
            indices[key].append(word)  

        return list(indices.values()) 
        