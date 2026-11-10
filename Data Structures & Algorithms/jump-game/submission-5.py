class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, nums[i] + i)

            else:
                return False

        return True