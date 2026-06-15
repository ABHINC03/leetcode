from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=Counter(nums)
        new_nums=dict(sorted(num.items(),key=lambda item:item[1]))
        return list((new_nums.keys()))[-1]