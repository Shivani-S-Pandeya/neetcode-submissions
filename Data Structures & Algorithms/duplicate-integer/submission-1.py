class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = {}
        for i, x in enumerate(nums):
            if x in storage:
                return True
            storage[x] = i
        return False