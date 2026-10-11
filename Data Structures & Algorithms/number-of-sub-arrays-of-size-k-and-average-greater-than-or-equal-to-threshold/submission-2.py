class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        number=0
        l=0
        S=0
        for R in range(len(arr)):
            if R-l+1>k :
                avg=S/k
                if avg>=threshold:
                    number+=1
                S-=arr[l]
                l+=1
                
            S+=arr[R]
        avg=S/k
        if avg>=threshold:
                    number+=1
        return number
            
            
            