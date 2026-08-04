class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxNum = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr = 0
                while num in numSet:
                    curr += 1
                    num += 1

                maxNum = max(maxNum, curr)

        return maxNum