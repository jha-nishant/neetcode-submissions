class Solution:
    def countBits(self, n: int) -> List[int]:
        ## Note we need 0 too in output
        result = []
        for i in range(n + 1): # this cant be range(1, n + 1)
            result.append(i.bit_count())
        return result