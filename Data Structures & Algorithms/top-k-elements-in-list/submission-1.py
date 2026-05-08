class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}

        for num in nums:
            if num in my_map:
                my_map[num] += 1
            else:
                my_map[num] = 1
        
        heap = []

        for key, value in my_map.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res