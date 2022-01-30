#User function Template for python3

import sys
sys.setrecursionlimit(10**6)


class Solution:

    def __init__(self):
        self.Time = 0
        
	def articulationPoints(self, V, adj):
        # code here

        ans = []
        visited = [False] * (V)
        time = [float("Inf")] * (V)
        lowest = [float("Inf")] * (V)

        ap = [False] * (V)
        
        def dfs(node,parent):
    
            children = 0
    
            visited[node]= True
    
            time[node] = self.Time
            lowest[node] = self.Time
            self.Time += 1
    
            for child in adj[node]:

                if visited[child] == False :
                    # parent[child] = node
                    children += 1
                    dfs(child,node)

                    # lowest[node] = min(lowest[node], lowest[child])
    
                    # if parent != -1 and lowest[child] >= time[node]:
                    #     ap[node] = True    
                        
                # elif child != parent: 
                #     lowest[node] = min(lowest[node], time[child])
                    
            if parent == -1 and children > 1:
                ap[node] = True
                return
            
            for child in adj[node]:
                if child!=parent:
                    lowest[node] = min(lowest[node], lowest[child])
            
            for child in adj[node]:
                if parent != -1 and lowest[child] >= time[node]:
                    ap[node] = True 

        
        for i in range(V):
            if visited[i]==0:
                dfs(i,-1)
                
        for i in range(V):
            if ap[i]==True:
                ans.append(i)
                
        return sorted(ans) if len(ans) > 0 else [-1]



 9 32
3 4
1 3
1 4
6 6
5 5
1 2
2 2
0 2
2 6
1 5
2 6
6 3
8 3
2 2
6 6
6 5
1 5
2 0
6 2
2 8
3 1
8 6
1 0
1 6
3 0
4 8
3 4
6 5
6 0
8 0
2 3
7 6


        
class Solution:
    
    def __init__(self):
        self.Time = 0
        
    def articulationPoints(self, V, adj):
        # code here

        ans = []
        visited = [False] * (V)
        time = [float("Inf")] * (V)
        lowest = [float("Inf")] * (V)

        ap = [False] * (V)
        
 
        def dfs(node,parent):
    
            children = 0
    
            visited[node]= True
    
            time[node] = self.Time
            lowest[node] = self.Time
            self.Time += 1
    
            for child in adj[node]:

                if visited[child] == False :
                    # parent[child] = node
                    children += 1
                    dfs(child,node)

                    lowest[node] = min(lowest[node], lowest[child])
    
                    if parent != -1 and lowest[child] >= time[node]:
                        ap[node] = True    
                        
                elif child != parent: 
                    lowest[node] = min(lowest[node], time[child])
                    
            if parent == -1 and children > 1:
                ap[node] = True
                return

        
        for i in range(V):
            if visited[i]==0:
                dfs(i,-1)
                
        for i in range(V):
            if ap[i]==True:
                ans.append(i)
                
        return sorted(ans) if len(ans) > 0 else [-1]



7 9
0 1
0 2
0 4
0 6
1 2
2 3
2 4
3 4
3 5



class Solution:
    time = 0
    def articulationPoints(self, V, adj):
        #Code here
        visited = [0]*V
        lowest_time = [float("inf")]*V
        time = [float('inf')]*V
        ans = [0]*V
        
        # print(adj)
        def dfs(node,parent):
            
            visited[node] = 1
            lowest_time[node] = self.time
            time[node] = self.time
            self.time+=1
            count = 0
            
            for child in adj[node]:
                if visited[child] == 0:
                    dfs(child,node)
                    count+=1
            
            for ch in adj[node]:
                if ch!=parent :
                    lowest_time[node] = min(lowest_time[node],lowest_time[ch])

            for childy in adj[node]:
                if lowest_time[childy] > time[node] and parent!=-1:
                    ans[node] = 1
                    ans[childy] = 1
                elif parent==-1 and count>1:
                    ans[node]=1
                    

            return
                
        for i in range(V):
            if visited[i]==0:
                dfs(i,-1)
        # print(ans)
        final = []
        for i in range(V):
            if ans[i]:
                final.append(i)
        return final

        