class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        seen = set()
        def dfs(index):
            if index == len(nums):
                res.append(perm.copy())
                return

            for i in nums:
                if i in seen:
                    continue

                perm.append(i)
                seen.add(i)
                dfs(index + 1)
                perm.pop()
                seen.remove(i)

        dfs(0)
        return res
