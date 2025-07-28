from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        d=deque(nums)
        d.rotate(k)
        nums[:]=list(d)
      
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        