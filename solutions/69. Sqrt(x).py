class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: return 0
        if x<4: return 1
        i = 1
        root = 1
        while root<=x:
            i += 1
            root = i*i
        return i-1
        
