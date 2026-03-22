from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=Counter(arr)
        l=[]
        for key,item in s.items():
            l.append(item)
            
        if len(l)==len(set(l)):
            return True
        else:
            return False
