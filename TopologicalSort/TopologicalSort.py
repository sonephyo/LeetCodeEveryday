from collections import deque

class Solution:
    def sort(self, vertices, edges):

        # TODO: Write your code here
        adj = []
        for _ in range(vertices):
            adj.append([-1 for _ in range(vertices)])

        for edge in edges:
            adj[edge[0]][edge[1]] = 1
            
        index = vertices - 1
        visited = [False] * vertices
        result = [-1] * vertices

        for i in range(vertices):
            if not visited[i]:
                index = self.dfs(adj, visited, result, index, i)

        return result
    
    def dfs(self, adj , visited, result, index, cur):
        
        if visited[cur]:
            return index
        
        visited[cur] = True
        
        for nextOne in range(len(adj)):
            if not visited[nextOne] and adj[cur][nextOne] == 1:
                index = self.dfs(adj, visited, result, index, nextOne)
        
        result[index] = cur
        index = index - 1
        
        return index
                
        





sol = Solution()
result = sol.sort(7,[[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])

