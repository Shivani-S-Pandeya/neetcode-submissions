class Solution:
    def isValid(self, s: str) -> bool:
        temp_stack = []
        pairs = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in "([{":
                temp_stack.append(ch)
            else:
                if not temp_stack:
                    return False
                if temp_stack[-1] != pairs[ch]:
                    return False
                else:
                    temp_stack.pop()
        return not temp_stack