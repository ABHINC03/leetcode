class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==1 and n==0:
            nums1=nums1
        elif m==0 and n==1:
            for i in range(n):
                nums1[i]=nums2[i]
        else:
            
            list1=[]
            for i in range(m):
                list1.append(nums1[i])
                
            for j in range(n):
                list1.append(nums2[j])
                
            list1.sort()
            for i in range(m+n):
                nums1[i]=list1[i]
        
     