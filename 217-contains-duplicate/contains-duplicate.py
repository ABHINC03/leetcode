class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di={keys:0 for keys in nums}
        for item in nums:
            di[item]+=1
        for keys in di:
            if di[keys]>1:
                return True
        return False

        