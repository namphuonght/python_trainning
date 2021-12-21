class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        result = ''
        carry = 0
        
        for i in range(max_len - 1, -1, -1):
            temp = carry
            temp += 1 if a[i] == '1' else 0
            temp += 1 if b[i] == '1' else 0
            
            result = ('1' if temp%2 == 1 else '0') + result            
            carry = 0 if temp < 2 else 1
            
        if carry != 0 : result = '1' + result
            
        return result