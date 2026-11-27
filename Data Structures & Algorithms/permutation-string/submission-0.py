from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        s2_count = {}
        s1_count = Counter(s1)

        # GROW: add s2[r]
        # CHECK + SHRINK: if the window is too big, drop s2[l] (delete if 0), l += 1
        # RECORD: if the window is full size and the counts match → return True
        # r += 1

        while r < len(s2):
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1 #Grow
            while (r-l + 1) > len(s1): #check
                s2_count[s2[l]] = s2_count.get(s2[l], 0) - 1 #decrease the count
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]] #delete if 0
                l += 1
            if (r-l + 1) == len(s1) and s2_count == s1_count: # record if the counts equal. Right after shrinking, the window is exactly full size, so you want to check it. That should be it's own IF
                return True
            r += 1
        return False