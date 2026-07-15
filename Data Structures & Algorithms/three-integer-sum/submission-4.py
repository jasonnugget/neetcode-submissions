class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for index, val in enumerate(nums):
            l = index + 1
            r = len(nums) - 1

            if val > 0:
                return res

            if index > 0 and val == nums[index - 1] and l < r:
                continue
            
            while(l < r):
                if val + nums[l] + nums[r] == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

                if val + nums[l] + nums[r] > 0:
                    r -= 1

                if val + nums[l] + nums[r] < 0:
                    l += 1

        return res


