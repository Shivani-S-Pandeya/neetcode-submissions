class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #the idea similar to two sums with o(1) space but with an outer loop for fixed number
        # nums[i] + nums[j] = - fixed_nums[i]

        #sort the input list first
        sorted_nums = sorted(nums)
        #initialize a final output list
        final_output = []
        for i, num in enumerate(nums):
            match = []
            l, r = i+1, len(nums) - 1
            #set value of fixed number ensuring it's not same number as prev. in the loop to avoid duplicate sets
            if sorted_nums[i] == sorted_nums[i-1] and i != 0:
                continue
            fixed = sorted_nums[i]
            
            #inner loop check starts against the fixed number from outer loop
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == -fixed:
                    match = [sorted_nums[l], sorted_nums[r], sorted_nums[i]]
                    final_output.append(match)
                    l += 1 #increment left pointer
                    r -= 1 #decrement right pointer

                    #increment right pointer until it isnt same as the previous l number 
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                elif sorted_nums[l] + sorted_nums[r] > -fixed:
                    r -= 1 #decrement right pointer
                else:
                    l +=1 #increment left pointer
        
        return final_output