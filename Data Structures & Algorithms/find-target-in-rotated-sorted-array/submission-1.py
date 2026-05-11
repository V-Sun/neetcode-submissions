class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        while l < r:
            mid = l + (r-l)//2
            if l == r:
                res = mid
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 

        if target <= nums[-1]:
            r = len(nums) - 1
        else:
            l = 0
            r = r - 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1