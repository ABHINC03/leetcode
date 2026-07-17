class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup= {num:i for i,num in enumerate(nums)}
        for i,num in enumerate(nums):
            if target-num in lookup and lookup[target-num]!=i:
                return sorted([lookup[target-num],i])

                



      
