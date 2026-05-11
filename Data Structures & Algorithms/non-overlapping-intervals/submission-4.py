class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # The start and end of our current interval
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]

        # How many intervals we have to remove
        rem_total = 0

        for start, end in intervals[1:]:
            if start < curr_end:
                curr_end = min(curr_end, end)
                rem_total += 1
            else:
                curr_start = start
                curr_end = end
        
        return rem_total

