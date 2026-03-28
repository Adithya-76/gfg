class Solution:
    def articulationPoints(self, V, edges):

        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        
        visited = [False] * V
        tin = [-1] * V
        low = [-1] * V
        mark = [False] * V 
        self.timer = 0
        
        
        def dfs(node, parent):
            visited[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1
            children = 0
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue 
                    
                if not visited[neighbor]:
                    children += 1
                    dfs(neighbor, node)
                    
                   
                    low[node] = min(low[node], low[neighbor])
                  
                    if parent != -1 and low[neighbor] >= tin[node]:
                        mark[node] = True
                else:
                   
                    low[node] = min(low[node], tin[neighbor])
            
            
            if parent == -1 and children > 1:
                mark[node] = True

       
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
                
        
        ans = []
        for i in range(V):
            if mark[i]:
                ans.append(i)
                
        if not ans:
            return [-1]
            
        return ans