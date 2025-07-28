class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l.reverse()
        b=' '.join(l)
        return b
        