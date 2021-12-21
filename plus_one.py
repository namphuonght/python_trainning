class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ''
        result = []
        for n in digits:
            strNum += str(n)
        sum_one = str(int(strNum) + 1)
        for s in sum_one:
            result.append(s)
            
        return result