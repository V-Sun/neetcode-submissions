class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r and r < len(nums) and l > i:
                if nums[l] + nums[i] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                if nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                if nums[l] + nums[i] + nums[r] < 0:
                    l += 1
            
        return res
                