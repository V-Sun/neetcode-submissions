class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        r = l = 0

        while r < len(nums) - 1:
            farthest = 0
            for num in range(l, r+1):
                farthest = max(farthest, num + nums[num])
            
            l = r + 1
            r = farthest
            res += 1

        return res