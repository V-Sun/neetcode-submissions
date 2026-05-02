class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence = {}

        for i in range(len(s)):
            lastOccurence[s[i]] = i
        
        res = []
        prev = 0
        iter = 0
        curEnd = 0
        while iter < len(s):
            curEnd = max(curEnd, lastOccurence[s[iter]])
            if iter == curEnd:
                res.append(iter-prev + 1)
                prev = iter + 1    
            iter += 1
        
        return res

                
            