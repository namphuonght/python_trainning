class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [n for n in str(int("".join(map(str, digits))) + 1)]