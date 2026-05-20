class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        missings=[]
        total=len(nums)
        sumoflist=(total*(total+1))/2
        sumofset=sum(set(nums))
        missing=sumoflist-sumofset
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                missings.append(nums[i])
                break
        missings.append(int(missing))
        return missings

        