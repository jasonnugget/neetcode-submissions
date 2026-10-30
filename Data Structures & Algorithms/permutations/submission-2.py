class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def dfs(index):
            if index == len(nums):
                res.append(perm.copy())
                return

            for i in nums:
                if i in perm:
                    continue

                perm.append(i)
                dfs(index + 1)
                perm.remove(i)

        dfs(0)
        return res
