# Constraints: 0 <= n <= 10^4

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return sum([n//5**num for num in range(1, 6)])