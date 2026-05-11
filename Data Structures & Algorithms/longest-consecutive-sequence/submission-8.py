class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Set of all numbers in our set
        numSet = set(nums)

        # Make a list of all the starting sequence numbers
        starts = []
        for num in numSet:
            if num - 1 not in numSet:
                starts.append(num)
        
        longest = 1
        for start in starts:
            curr = start
            while curr in numSet:
                curr += 1
            longest = max(longest, curr - start)
        
        return longest
            
            
        