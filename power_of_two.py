class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            return (n & (n-1)) == 0