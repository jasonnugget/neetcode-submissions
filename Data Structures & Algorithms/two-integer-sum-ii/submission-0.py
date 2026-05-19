class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        setNumbers = set(numbers)

        for i, j in enumerate(numbers):
            k = target - j

            if k in setNumbers:
                for a in range(len(numbers)):
                    if k == numbers[a]:
                        return [i + 1, a + 1]