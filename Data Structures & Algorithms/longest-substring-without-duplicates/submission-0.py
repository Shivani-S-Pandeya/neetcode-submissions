class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #setting the window start and end index
        l = r = 0
        curr_window_set = set()
        longest = 0
        while r < len(s):
            if s[r] not in curr_window_set:
                curr_window_set.add(s[r])
                longest = max(longest, (r-l)+1) #no. elements in the window right - left + 1 
                r += 1
            else:
                while s[r] in curr_window_set:
                    curr_window_set.remove(s[l])
                    l += 1
        return longest