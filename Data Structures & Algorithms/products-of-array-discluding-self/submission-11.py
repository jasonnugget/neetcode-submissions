class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [[] for i in range(len(nums))]

        pre = 1
        for i in range(len(nums)):
            sol[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums) - 1, -1, -1):
            sol[j] *= post
            post *= nums[j]

        return sol