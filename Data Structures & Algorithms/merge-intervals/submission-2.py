class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = intervals[0]

        for i in range(len(intervals)):
            if intervals[i][0] > cur[1]:
                res.append(cur)
                cur = intervals[i]
            if intervals[i][0] <= cur[1]:
                cur = [min(intervals[i][0], cur[0]), max(intervals[i][1], cur[1])]
            
        
        res.append(cur)
        return res

        