class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            stack = []
            temp = temperatures[i]
            curr = i
            found = False  # CHANGED: track whether we actually found a warmer day
            while curr < len(temperatures):
                if temperatures[curr] <= temp:
                    stack.append(temperatures[curr])
                    curr += 1
                else:
                    found = True  # CHANGED: set flag when we break on a warmer day
                    break
            
            if found:  # CHANGED: only count gap if a warmer day exists, else leave res[i] = 0
                curr = 0
                while stack:
                    curr += 1
                    stack.pop()
                
                res[i] = curr
        return res
