class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        maxNum = 1

        l, r = 0, 1
        seen = set()
        seen.add(s[l])
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                maxNum = max(maxNum, r - l + 1)
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        return maxNum
