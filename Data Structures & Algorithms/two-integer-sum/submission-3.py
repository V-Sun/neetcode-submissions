class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        res = []
        for idx, num in enumerate(nums):
            if target - num in myDict:
                res.append(myDict[target-num])
                res.append(idx)
            else:
                myDict[num] = idx
        
        return res
