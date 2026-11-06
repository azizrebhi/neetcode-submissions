class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer=0
        L=[]
        while pointer<len(word1) and pointer<len(word2):
            L.append(word1[pointer])
            L.append(word2[pointer])
            pointer+=1
            
        if pointer>=len(word1):
            L.append(word2[pointer:])
        else :
            L.append(word1[pointer:])
        return "".join(L)