class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert the list to a set
        s = set(nums)
        longest = 0 # longest consecutive sequence

        #find the 'starts' of consecutivity
        res = []
        for num in s:
            if num-1 not in s:
                res.append(num)
        
        #find the consecutive sequence from each of the start
        for start in res:
            count = 0
            while (start+count) in s:
                count += 1
                longest = max(longest, count) #find the 'longest' sequence
        return longest