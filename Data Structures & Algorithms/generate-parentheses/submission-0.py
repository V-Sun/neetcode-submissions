class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, open, close):
            if open == n and close == n:
                res.append(cur)
                return
            
            if close > open:
                return
            
            if open == n:
                cur += ")"
                dfs(cur, open, close + 1)
            else:
                cur += "("
                dfs(cur, open + 1, close)
                cur = cur[:-1]
                cur += ")"
                dfs(cur, open, close + 1)
        
        dfs("", 0, 0)
        return res

            

