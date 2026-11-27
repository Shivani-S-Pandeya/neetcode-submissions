class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        counts = {}
        longest = 0
        
        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1
            changes_needed = (r-l+1) - max(counts.values()) #total len. of window - max count of char
            
            while changes_needed > k: # becomes invalid; so shrink until it becomes valid
                counts[s[l]] = counts.get(s[l], 0) - 1 # drop the letter first to shrink the window
                l += 1 #increment l 
                changes_needed = (r-l+1) - max(counts.values()) # recalculate
            longest = max(longest, r-l+1)
            r += 1  # increment r after len of window calculation is done
        
        return longest 