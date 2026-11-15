class Solution:
    def rob(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0

        for n in nums:
            num1 = max(num2, num1 + n)
            temp = num2
            num2 = num1
            num1 = temp

        return num2