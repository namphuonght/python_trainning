class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                result = nums[i]
                count = 1
            elif nums[i] == result:
                count += 1
            else:
                count -= 1
        
        return result
                