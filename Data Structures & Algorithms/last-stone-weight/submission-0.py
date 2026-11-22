import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for n in stones:
            heapq.heappush(max_heap, -n)
        while len(max_heap) >= 2:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x != y:
                diff = x-y #don't need abs() since x is always >= y
                heapq.heappush(max_heap, -diff)
        if max_heap:
            return -max_heap[0]
        return 0
        