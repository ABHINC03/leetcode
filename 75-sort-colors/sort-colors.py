class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums=self.mergeSort(nums)
        for i in range(len(sorted_nums)):
            nums[i]=sorted_nums[i]

    def mergeSort(self, arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result