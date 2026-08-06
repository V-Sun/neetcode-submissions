class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {n: [] for n in range(n)}

        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        visited = set()

        def dfs(node, prev) -> None:
            visited.add(node)
            for nei in adjMap[node]:
                if nei == prev:
                    continue
                if nei in visited:
                    return False
                dfs(nei, node)
            return True
        
        return dfs(0,-1) and len(visited) == n
