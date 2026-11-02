class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            total =  digits[i] + carry
            res.append(total % 10)
            carry = total // 10

        if carry != 0:
            res.append(carry)

        res.reverse()
        return res