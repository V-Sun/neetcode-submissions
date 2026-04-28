class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(remaining, cur):
            res.append(cur.copy())
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i-1]:
                    continue
                cur.append(remaining[i])
                dfs(remaining[i+1:], cur)
                cur.pop()
        
        dfs(nums, [])
        return res