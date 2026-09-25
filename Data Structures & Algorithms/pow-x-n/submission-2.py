import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        num = self.myPowPositive(x, abs(n))
        if n < 0:
            return 1 / num
        return num
    
    def myPowPositive(self, x: float, n: int) -> float:
        if n == 1:
            return x
        half = int(n / 2)
        odd = n % 2
        half_power = self.myPow(x, half)
        out = half_power * half_power
        if odd:
            out *= x
        
        return out