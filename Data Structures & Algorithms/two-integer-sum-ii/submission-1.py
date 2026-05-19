class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while( i < j):

            compute = numbers[i] + numbers[j]

            if(compute == target):
                return [i + 1, j + 1]

            elif(compute > target):
                j -= 1

            elif(compute < target):
                i += 1

            