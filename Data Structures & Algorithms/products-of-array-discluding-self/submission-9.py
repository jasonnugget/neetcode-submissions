class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []

        left = 1
        for i in range(len(nums)):
            if i == 0:
                sol.append(left)
            else:
                left = left * nums[i - 1]
                sol.append(left)

        nums.reverse()

        right = 1
        postfix = []
        for j in range(len(nums)):
            if j == 0:
                postfix.append(right)
            else:
                right = right * nums[j - 1]
                postfix.append(right)

        postfix.reverse()

        for c in range(len(nums)):
            sol[c] = sol[c] * postfix[c]

        return sol