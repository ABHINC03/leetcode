class Solution:
    def reverse(self, x: int) -> int:

        
        

        if x<0:
            x=-1*x
            x=str(x)
            l1=list(x)
            l1.reverse()
            x=''.join(l1)
            x=int(x)
            x=-1*x
           
        else:
            x=str(x)
            l1=list(x)
            l1.reverse()
            x=''.join(l1)
            x=int(x)
            
        INT_MIN = -2**31        # -2147483648
        INT_MAX = 2**31 - 1     # 2147483647
        if x< INT_MIN or x > INT_MAX:
            return 0
        return x
        
        
        

        
        
            


