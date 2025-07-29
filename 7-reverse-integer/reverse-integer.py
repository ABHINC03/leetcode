class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31        
        INT_MAX = 2**31 - 1
        sign=1    
        if x<0:
            sign=-1
            x=abs(x)
        x=str(x)
        rev=''.join(reversed(x))
        x=int(rev)
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return sign*x
        
        
        
        

        
        
            


