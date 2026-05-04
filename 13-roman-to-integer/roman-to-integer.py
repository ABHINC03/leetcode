class Solution:
    def romanToInt(self, s: str) -> int:
        di={'I':1,'V':5,"X":10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        prev=0
        for char in reversed(s):
            if di[char]<prev:
                total-=di[char]
            else:
                total+=di[char]
            prev=di[char]
        return total