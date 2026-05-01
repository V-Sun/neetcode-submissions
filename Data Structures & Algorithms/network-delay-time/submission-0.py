class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        quickest = [-1] * (n+1)

        adjMap = {i+1:[] for i in range(n)}
        
        for ui, vi, ti in times:
            adjMap[ui].append((vi,ti))
        
        visited = set()

        def dfs(node, curTime):
            if quickest[node] == -1:
                quickest[node] = curTime
                for vi, cost in adjMap[node]:
                    dfs(vi, quickest[node]+cost)

            if curTime < quickest[node]:
                quickest[node] = min(quickest[node], curTime)
                for vi, cost in adjMap[node]:
                    dfs(vi, quickest[node]+cost)
            else:
                return
        
        dfs(k, 0)

        if -1 in quickest[1:]:
            return -1
        return max(quickest[1:])
