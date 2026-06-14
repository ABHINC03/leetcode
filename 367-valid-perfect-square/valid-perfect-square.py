class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num**0.5
        if x.is_integer():
            return True
        else:
            return False