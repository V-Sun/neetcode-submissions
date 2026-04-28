class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(remaining, cur):
            if len(remaining) == 0 or len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(remaining)):
                cur.append(remaining[i])
                dfs(remaining[:i] + remaining[i+1:], cur)
                cur.pop()
        
        dfs(nums, [])
        return res