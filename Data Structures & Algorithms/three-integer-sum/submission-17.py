class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if nums[i] != nums[i - 1] or i == 0:
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0:
                        sol.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1

                    else:
                        l += 1

        return sol