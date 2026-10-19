class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(index, permu, count, seen):
            if index in seen:
                return

            permu.append(nums[index])
            count += 1

            if count == len(nums):
                res.append(permu.copy())
                permu.pop()
                return

            seen.append(index)

            for i in range(len(nums)):
                dfs(i, permu, count, seen)

            permu.pop()
            seen.remove(index)

        for i in range(len(nums)):
            dfs(i, [], 0, [])

        return res
        