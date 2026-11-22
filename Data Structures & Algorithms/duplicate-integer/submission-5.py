class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, x in enumerate(nums):
            if x in seen:
                return True
            seen.add(x)
        return False

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         my_set = set(nums)
#         if (len(my_set) != len(nums)):
#             return True
#         else:
#             return False

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         storage = {}
#         for i, x in enumerate(nums):
#             if x in storage:
#                 return True
#             storage[x] = i
#         return False