class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # Valid Triplets are any triplets whose max value is less than the target numbers
        validTrips = []

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            validTrips.append([a,b,c])
        
        res = [0] * 3
        for trip in validTrips:
            for i in range(3):
                if trip[i] == target[i]:
                    res[i] = 1
        
        return 0 not in res
        
                