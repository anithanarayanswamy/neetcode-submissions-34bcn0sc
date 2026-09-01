class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dictNum = {}

       for i,n in enumerate(nums):
        diff = target - n
        if diff in dictNum:
            return [dictNum[diff], i]
        dictNum[n] = i