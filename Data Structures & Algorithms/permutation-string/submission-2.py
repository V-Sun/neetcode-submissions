class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = {c:0 for c in s1}
        for c in s1:
            s1_set[c] += 1

        print(s1_set)
        if len(s1) > len(s2):
            return False
        
        for i in range(0, len(s2) - len(s1) + 1):
            s2_set = {c:0 for c in s2[i:i+len(s1)]}
            for c in s2[i:i+len(s1)]:
                s2_set[c] += 1
            if s1_set == s2_set:
                print(s2_set)
                return True
        
        return False
