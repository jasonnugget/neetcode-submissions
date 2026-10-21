class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        pSpeed = reversed(sorted(zip(position, speed)))

        for p,s in pSpeed:
            if stack:
                if stack[-1] < (target - p) / s:
                    stack.append((target - p) / s)
                
                else:
                    continue

            else:
                stack.append((target - p) / s)

        return len(stack)