class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=[False]*len(nums)
        def backtrack(current_path):
            if len(current_path)==len(nums):
                result.append(list(current_path))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                current_path.append(nums[i])
                backtrack(current_path)
                current_path.pop()
                used[i]=False
        backtrack([])
        return result
        