class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def solve(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if memo[num] != -1:
                return memo[num]
            result = solve(num - 1) + solve(num - 2)
            memo[num] = result
            return result
        return solve(n)