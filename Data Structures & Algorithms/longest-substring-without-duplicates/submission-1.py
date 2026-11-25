class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        current_window_set = set()
        longest = 0

        while r < len(s):
            if s[r] not in current_window_set:
                current_window_set.add(s[r])
                longest = max(longest, (r-l)+1)
                r += 1
            else: # the character is repeating
                while s[r] in current_window_set: 
                    current_window_set.remove(s[l]) #remove the character from the set from left index to see the current window
                    l += 1 #shrink the window by incrementing the l
        return longest

