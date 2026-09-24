class Solution:
    def hammingWeight(self, n: int) -> int:
        # # elaborate way
        # a = format(n, 'b')
        # print(type(a)) -> String
        # count 1
        return n.bit_count()
        