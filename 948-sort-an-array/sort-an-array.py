class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        sorted_nums=self.mergesort(nums)
        

        nums[:]=sorted_nums
        return nums
        
    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=self.mergesort(arr[:mid])
        right=self.mergesort(arr[mid:])
        return self.merge(left,right)
    def merge(self,left,right):
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i=i+1
            else :

                result.append(right[j])
                j+=1
        while i<len(left):
            result.append(left[i])
            i+=1
        while j<len(right):
            result.append(right[j])
            j+=1
        return result