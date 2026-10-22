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

        def dfs(seen, perms, index):
            if len(perms) == len(digits):
                res.append(perms)

            for i in range(len(digits)):
                if i >= index:
                    index += 1
                    for char in numbers[int(digits[i])]:
                        if char in seen:
                            continue

                        perms += char

                        dfs(seen, perms, index)

                        perms = perms[:-1]

        dfs(set(), "", 0)
        return res