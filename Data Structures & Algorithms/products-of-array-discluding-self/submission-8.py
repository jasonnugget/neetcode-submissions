class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        leftTotal = 1
        for i in range(len(nums)):
            if i == 0:
                left.append(leftTotal)
            else:
                leftTotal = leftTotal * nums[i - 1]
                left.append(leftTotal)

        rightTotal = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right.append(rightTotal)
            else:
                rightTotal = rightTotal * nums[i + 1]
                right.append(rightTotal)
            
        right.reverse()

        sol = []
        for i in range(len(nums)):
            if i == 0:
                sol.append(right[i])
            elif i == len(nums) - 1:
                sol.append(left[i])
            else:
                sol.append(left[i] * right[i])
        

        return sol
