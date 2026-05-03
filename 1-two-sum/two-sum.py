class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i ,num in enumerate(nums):
            for j,num1 in enumerate(nums):
                if i!=j:
                    if num+num1==target:
                        return [i,j]