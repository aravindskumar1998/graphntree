from heapq import *
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        mst = [False]*V
        weights = [float('inf')]*V
        parent = [-1]*V
        
        weights[0] = 0
        # mst[0] = True
        heap = [(0,0)]
        
        
        for i in range(V):
            _,node = heappop(heap)
            while mst[node]==True:  ##Important
                _,node = heappop(heap)
            mst[node]=True
            for child, wech in adj[node]:
                if mst[child]==False and wech < weights[child]:
                    heappush(heap,(wech,child))
                    weights[child]=wech
                    parent[child]=node
               
        sums = 0
        for w in weights:
            sums+=w
        return sums
                