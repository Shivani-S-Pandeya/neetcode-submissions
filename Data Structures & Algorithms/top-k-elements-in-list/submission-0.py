import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        #Use counter to get the frequency/count of each
        counts = Counter(nums)
        for key, value in counts.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k: #if min-heap grows larger than k, then pop
                heapq.heappop(min_heap)
        return [key for value, key in min_heap] 