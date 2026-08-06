class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        cur_end = intervals[0][1]
        
        rmv = 0
        for interval in intervals:
            if interval[0] < cur_end:
                cur_end = min(cur_end, interval[1])
                rmv += 1
            else:
                cur_end = interval[1]
        
        return rmv - 1


