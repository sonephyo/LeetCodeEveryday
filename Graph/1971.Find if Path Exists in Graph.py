class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        visited = [False] * n
        q = deque()

        neighbours = defaultdict(list)
        for i in edges:
            neighbours[i[0]].append(i[1])
            neighbours[i[1]].append(i[0])
        
        visited[source] = True
        q.append(source)

        while q:
            currentVertex = q.popleft()
            print(currentVertex)
            if currentVertex == destination:
                return True
            for neighbour in neighbours[currentVertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)

                
        return False