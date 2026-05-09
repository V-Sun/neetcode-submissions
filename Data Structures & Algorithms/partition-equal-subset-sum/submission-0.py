class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        memo = {}
        
        total = total // 2

        def backtrack(idx, curr):
            if curr == total:
                return True
            if curr > total or idx >= len(nums):
                return False
            
            if (idx, curr) in memo:
                return memo[idx,curr]

            take = backtrack(idx+1, curr + nums[idx])
            skip = backtrack(idx+1, curr)

            memo[(idx, curr)] = take or skip

            return memo[(idx, curr)]
        
        return backtrack(0,0)
            