class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        total = 0
        idx = 0
        for i in range(len(gas)):
            total = total - cost[i] + gas[i]
            if total < 0:
                idx = i + 1
                total = 0
        
        return idx
