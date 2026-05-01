class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        zipped = [(p, s) for p, s in zip(position, speed)]
        zipped.sort(reverse=True)
        stack = []

        for p, s in zipped:
            t = (target - p) / s
            stack.append(t)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
            
        return len(stack)

            