class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            
            while True and stack:
                if stack[-1][0] < temperatures[i]:
                    cur = stack.pop()[1]
                    res[cur] = i - cur
                else:
                    break
            stack.append((temperatures[i], i))
        
        while stack:
            cur = stack.pop()[1]
            res[cur] = 0


        return res

        
        
