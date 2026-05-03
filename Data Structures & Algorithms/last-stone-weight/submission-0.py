class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            stone = stone * -1
            heapq.heappush(heap, stone)
        
        while len(heap) > 1:
            temp1 = heapq.heappop(heap) * -1
            temp2 = heapq.heappop(heap) * -1
            if temp1 == temp2:
                continue
            else:
                heapq.heappush(heap, (temp1 - temp2) * -1)
        
        if not heap:
            return 0
        return heap[0] * -1

        