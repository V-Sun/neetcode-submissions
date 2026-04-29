class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjMap = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adjMap[node1].append(node2)
            adjMap[node2].append(node1)

        totalComp = 0

        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)
            for n in adjMap[node]:
                if n == prev:
                    continue
                else:
                    dfs(n, node)
        
        for node in range(n):
            if node in visited:
                continue
            else:
                totalComp += 1
                dfs(node, -1)
        
        return totalComp
