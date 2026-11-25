import heapq
from collections import Counter
#pop out the smallest until k bigger elements are left
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        count_nums = Counter(nums) # {1: 3, 2: 2, 100: 1}  number -> how often
        for key, value in count_nums.items(): # (1,3), (2,2), (100,1)
            heapq.heappush(min_heap, (value,key)) # push (count, number)
            while len(min_heap) > k:        # more than k items?
                heapq.heappop(min_heap) # drop the one with the smallest count
        result = [item[1] for item in min_heap] # keep only the numbers
        return result 