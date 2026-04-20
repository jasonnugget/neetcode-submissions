class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for i in range(len(nums)):
            for j in range(len(arr)):
                if nums[i] == arr[j]:
                    return True
            arr.append(nums[i])
        return False