class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1 = 0
        cost2 = 0

        for c in cost:
            temp = min(cost1, cost2) + c
            cost1 = cost2
            cost2 = temp

        return min(cost1, cost2)