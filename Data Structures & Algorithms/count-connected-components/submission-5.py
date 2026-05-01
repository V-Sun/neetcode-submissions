class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjMap = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adjMap[node1].append(node2)
            adjMap[node2].append(node1)

        def dfs(node, par):
            if node == None:
                return
            visited.add(node)
            for next in adjMap[node]:
                if next == par or next in visited:
                    continue
                else:
                    dfs(next, node)
        
        count = 0
        for node in range(n):
            if node in visited:
                continue
            else:    
                count += 1
                dfs(node, -1)

        return count