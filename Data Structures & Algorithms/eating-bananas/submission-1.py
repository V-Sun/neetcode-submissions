class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        low, high = 1, k

        res = -1
        while low <= high:
            mid = low + (high - low)//2
            total_hours = 0
            for banana in piles:
                total_hours += math.ceil(banana/mid)
            if total_hours <= h:
                res = mid
            if total_hours > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return res
        
        
