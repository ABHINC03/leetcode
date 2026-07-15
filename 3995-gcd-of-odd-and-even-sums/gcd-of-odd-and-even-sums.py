import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        lastodd=2*n-1
        lasteven=2*n
        firstodd=1
        firsteven=2
        sumodd=n/2*(firstodd+lastodd)
        sumeven=n/2*(firsteven+lasteven)
        return math.gcd(int(sumodd),int(sumeven))