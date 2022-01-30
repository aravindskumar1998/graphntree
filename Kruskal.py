from heapq import *
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        ##KRUSKAL ALGO
        
        parent = [i for i in range(V)]
        rank = [0]*V
        edges = []
        mstedges = []
        for node in range(V):
            for child, weight in adj[node]:
                edges.append((weight,node,child))
                
        edges.sort()
        
        def findParent(node):
            if parent[node]==node:
                return node
            parent[node] = findParent(parent[node])
            return parent[node]
            
        def unionFn(edge):
            weight, u, v = edge
            u = findParent(u)
            v = findParent(v)
            if u==v:
                return None
            if rank[u]>rank[v]:
                parent[v] = u
            elif rank[u]<rank[v]:
                parent[u] = v
            else:
                parent[u] = v
                rank[v]+=1
            return edge
        
        sums = 0
        for edge in edges:
            mstEdge = unionFn(edge)
            if mstEdge:
                mstedges.append(mstEdge)
                sums+=mstEdge[0]
                
        return sums