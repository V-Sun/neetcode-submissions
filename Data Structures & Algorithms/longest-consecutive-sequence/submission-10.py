class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        starts = []
        maxNum = 0
        for num in nums:
            if num - 1 not in numSet:
                starts.append(num)
        
        for start in starts:
            curr = 0
            while start in numSet:
                curr += 1
                start += 1
            maxNum = max(curr, maxNum)

        return maxNum