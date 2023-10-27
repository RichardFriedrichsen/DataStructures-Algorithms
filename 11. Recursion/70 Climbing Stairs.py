# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def __init__(self) -> None:
        self.total = 0

    def climbStairs(self, n: int) -> int:
        if n == 1:
            self.total += 1
            return 1
        elif n == 2:
            self.total += 2
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        


n = 8
solution = Solution()
solution.climbStairs(n)
print(solution.total)