class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                target = 0 - nums[i]
                
                while l < r:
                    if nums[l] + nums[r] == target:
                        sol.append([nums[l], nums[r], nums[i]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif nums[l] + nums[r] > target:
                        r -= 1

                    else:
                        l += 1



        return sol
