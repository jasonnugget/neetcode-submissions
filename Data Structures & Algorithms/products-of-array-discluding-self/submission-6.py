class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[0])
            
            else:
                prefix.append(nums[i] * prefix[i - 1])

        reverseNums = nums[::-1]
        postfix = []
        for i in range(len(reverseNums)):
            if i == 0:
                postfix.append(reverseNums[i])
            
            else:
                postfix.append(reverseNums[i] * postfix[i - 1])

        postfix = postfix[::-1]

        sol = []

        for i in range(len(nums)):
            if i == 0:
                sol.append(postfix[i + 1])
            
            elif i == len(nums) - 1:
                sol.append(prefix[i - 1])

            else:
                sol.append(prefix[i - 1] * postfix[i + 1])

        return sol

