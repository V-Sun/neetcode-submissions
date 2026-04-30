class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for i in nums:
            length = 1
            while (i + length) in num_set:
                length += 1
            max_length = max(max_length, length)

        return max_length