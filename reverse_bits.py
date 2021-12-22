class Solution:
    def reverseBits(self, n: int) -> int:
        return (int('{:032b}'.format(int(n))[::-1], 2)