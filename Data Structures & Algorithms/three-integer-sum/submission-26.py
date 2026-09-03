class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                return res

            if nums[i] != nums[i - 1] or i == 0:
                while l < r:
                    if nums[i] + nums[l] + nums[r] > 0:
                        r -= 1

                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1

                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

        return res