class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                sum = digits[i] + 1
            else:
                sum = digits[i] + carry
            digits[i] = sum%10
            carry = sum//10
        if carry == 1:
            digits.insert(0, carry)
            
        return digits
        