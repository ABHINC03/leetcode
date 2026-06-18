class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return [-1,-1]


        l=0
        r=len(nums)-1
        
        while (l<=r):
            mid=int((l+r)/2)
            if nums[mid]==target:
                left=mid
                right=mid
                while left>0 and nums[left-1]==target:
                    left-=1
                while right<len(nums)-1 and nums[right+1]==target:
                    right+=1
                return [left,right]
            
            
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return [-1,-1]
        