class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        
        freq_map = {}

        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1
        
        heap = [-v for k, v in freq_map.items()]
        heapq.heapify(heap)
        queue = deque([])

        while heap or queue:
            time += 1
            if heap:
                temp = heapq.heappop(heap)
                if temp + 1 != 0:
                    queue.append((time + n, temp + 1))

            while True:
                if queue:
                    if queue[0][0] == time:
                        heapq.heappush(heap, queue.popleft()[1])
                    else:
                        break
                break
        
        return time
            
            
                

        
        