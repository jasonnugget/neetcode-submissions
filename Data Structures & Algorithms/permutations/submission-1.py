class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(seen, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())

            for i in range(len(nums)):
                if i in seen:
                    continue

                perm.append(nums[i])
                seen.add(i)

                dfs(seen, perm)

                perm.pop()
                seen.remove(i)

        
        dfs(set(), [])

        return res