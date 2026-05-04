
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1=s.split()
        l=len(list1)
        s=str(list1[l-1])
        return len(s)
