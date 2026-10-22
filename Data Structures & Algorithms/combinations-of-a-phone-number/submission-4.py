class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numbers = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }

        res = []

        def dfs(perms, index):
            if len(perms) == len(digits):
                res.append(perms)
                return

            for char in numbers[int(digits[index])]:
                dfs(perms + char, index + 1)

        dfs("", 0)
        return res