class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])

            else:
                prefix.append(nums[i] * prefix[i - 1])

        postfixNums = nums[::-1]
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                postfix.append(postfixNums[i])

            else:
                postfix.append(postfixNums[i] * postfix[i - 1])

        postfix = postfix[::-1]

        sol = []
        for i in range(len(nums)):
            if i == 0:
                sol.append(postfix[1])

            elif i == len(nums) - 1:
                sol.append(prefix[i - 1])

            else:
                sol.append(prefix[i - 1] * postfix[i + 1])

        return sol