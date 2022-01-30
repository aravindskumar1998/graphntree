#User function Template for python3

class Solution:
    
    def __init__(self):
        self.time = 0
   
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        # code here
        visited = [0]*V
        lowest_time = [float("inf")]*V
        time = [float('inf')]*V
        ans = []
        # print(adj)
        
        def dfs(node,parent):
            
            visited[node] = 1
            lowest_time[node] = self.time
            time[node] = self.time
            self.time+=1
            
            for child in adj[node]:
                if visited[child] == 0:
                    dfs(child,node)
            
            for ch in adj[node]:
                if ch!=parent :
                    lowest_time[node] = min(lowest_time[node],lowest_time[ch])

            for childy in adj[node]:
                if lowest_time[childy] > time[node]:
                    ans.append((childy, node))

            return
                
        for i in range(V):
            if visited[i]==0:
                dfs(i,-1)
        # print(ans)
        if (c,d) in ans or (d,c) in ans:
            return 1
        return 0
