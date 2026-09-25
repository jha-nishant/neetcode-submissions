class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        start = n
        while start not in seen:
            if start == 1:
                break
            seen.add(start)
            start = self.digitSqSum(start)
        return start == 1
    
    def digitSqSum(self, n: int) -> int:
        sqSum = 0
        while n > 0:
            rem = n % 10
            sqSum += rem * rem
            n = int(n / 10)
        return sqSum
