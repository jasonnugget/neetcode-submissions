class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]

        test = set(nums)

        if 0 not in test:
            for i in nums:
                res.append(total // i)

            return res

        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zeroCount == 0:
                    zeroCount += 1
                    res.append(total)

                else:
                    newRes = []
                    for i in range(len(nums)):
                        newRes.append(0)

                    return newRes

            else:
                res.append(0)
        return res



