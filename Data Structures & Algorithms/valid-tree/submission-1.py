class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjSet = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adjSet[node1].append(node2)
            adjSet[node2].append(node1)
    

        curVisit = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adjSet[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True
            

        
        return dfs(0, -1) and len(visited) == n