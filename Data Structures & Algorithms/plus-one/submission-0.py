class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringNum = ""
        for nums in digits:
            stringNum += str(nums)

        stringNum = int(stringNum)
        stringNum += 1

        res = []
        for i in str(stringNum):
            res.append(int(i))

        return res