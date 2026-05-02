class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        adjMap = {i:[] for i in range(len(points))}
        visited = set()
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjMap[i].append([cost, j])
                adjMap[j].append([cost, i])
        

        res = 0
        minH = [[0,0]]
        while len(visited) < len(points):
            cost, i = heapq.heappop(minH)
            if i in visited: 
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adjMap[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        
        return res

            
        
        