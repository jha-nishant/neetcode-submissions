class Solution:
    def hammingWeight(self, n: int) -> int:
        # format(n, 'b') -> string
        return n.bit_count()
        