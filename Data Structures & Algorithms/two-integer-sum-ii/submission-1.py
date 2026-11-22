class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        result = []
        while (l < r):
            if numbers[l] + numbers[r] == target:
                result = [l+1, r+1]
                return result
            elif numbers[l] + numbers[r] > target:
                r -= 1 # decrease the right pointer if the value is greater
            else:
                l += 1 #increase the left pointer if value is smaller