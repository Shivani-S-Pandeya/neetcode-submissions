"""
strs = ["Hello","World"]          ← input list
encoded = encode(strs)            ← your drill 14: "5#Hello5#World"
result = decode(encoded)          ← your drill 15: ["Hello","World"]
result == strs ?                  ← that's the check
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0 #create your own index so that you jump to the next word
        decoded_result = [] #decoded list 
        while (i < len(s)):
            j = s.find("#",i) #get the index which has #
            length = int(s[i:j]) #get the length of word before that # by slicing
            start = j + 1 
            end = start + length #note that in slice; the end position is the exact index. length = end - start
            word = s[start:end] #end is exclusice
            decoded_result.append(word) # add to the list
            i = end # move/jump i past the word
        return decoded_result