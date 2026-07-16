class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results=[]
        current=[]
        def backtrack(index):
            if index==len(nums):
                results.append(list(current))
                return
            current.append(nums[index])
            backtrack(index+1)
            current.pop()
            backtrack(index+1)
        backtrack(0)
        return results