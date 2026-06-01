import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(0, n + 1):
           adj[i] = [] 
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))
            
        shortest = {}
        minHeap = [[-1.0, start_node]]
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = -w1
            if n1 == end_node:
                return -w1
                
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    prob_positive = (-w1) * w2
                    heapq.heappush(minHeap, [-prob_positive, n2])
                    
        return 0.0
