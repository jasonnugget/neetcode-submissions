class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArray = []
        for i, j in enumerate(nums):
            multiplicand = 1
            for a, b in enumerate(nums):
                if i != a:
                    multiplicand *= b
            outputArray.append(multiplicand)
        
        return outputArray
                    
        