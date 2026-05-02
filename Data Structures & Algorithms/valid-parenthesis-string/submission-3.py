class Solution:
    def checkValidString(self, s: str) -> bool:
        maxLeft = 0
        minLeft = 0

        for c in s:
           
            if c == '(':
                maxLeft += 1
                minLeft += 1
            elif c == '*':
                minLeft -= 1
                maxLeft += 1
            if c == ')':
                maxLeft -= 1
                minLeft -= 1

            if maxLeft < 0:
                return False
            minLeft = max(minLeft, 0)
        
        if minLeft <= 0 and maxLeft >= 0:
            return True
        return False