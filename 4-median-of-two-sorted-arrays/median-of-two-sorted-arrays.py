class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for nums in nums2:

            nums1.append(nums)
        nums1.sort()
    
        l=len(nums1)
        if l%2==0:
            l=l//2
            return (nums1[l-1]+nums1[l])/2
        else:
            l=(l+1)//2
            return nums1[l-1]
         