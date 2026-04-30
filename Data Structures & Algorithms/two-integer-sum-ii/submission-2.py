class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        res = []

        while start < end:
            if numbers[start] + numbers[end] == target:
                res.append(start+1)
                res.append(end+1)
                break
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        
        return res
