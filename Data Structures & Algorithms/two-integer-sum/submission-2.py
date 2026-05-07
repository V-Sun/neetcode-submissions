class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            if target - nums[i] in my_map:
                return [my_map.get(target - nums[i]), i]
            else:
                my_map[nums[i]] = i
        
        return [-1,-1]