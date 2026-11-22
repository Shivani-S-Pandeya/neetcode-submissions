class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #product of eveything on the left
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        #product of everything on the right 
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right #res[i] already has left side value * right
            right *= nums[i]
            
        return res