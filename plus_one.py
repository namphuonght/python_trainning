class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ''
        for n in digits:
            strNum += str(n)
        return [s for s in str(int(strNum)+1)]
        