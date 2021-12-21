class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min = float('+inf')
        result = []
        arr.sort()
        
        for i in range(1, len(arr)):
            dif = arr[i] - arr[i - 1]
            if dif == min:
                result.append([arr[i - 1], arr[i]])
            elif dif < min:
                result = [[arr[i - 1], arr[i]]]
                min = dif
                       
        return result