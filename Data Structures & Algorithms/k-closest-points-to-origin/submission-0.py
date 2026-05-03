class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.sqrt((x1)**2 + (y1)**2), [x1,y1]) for x1, y1 in points]
        heapq.heapify(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
