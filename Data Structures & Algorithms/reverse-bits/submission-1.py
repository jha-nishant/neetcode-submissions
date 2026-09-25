class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverseBitsWithoutBitwise(n)

    def reverseBitsWithBitwise(self, n: int) -> int:
        # special bitwise logic can be applied
        # Implement that
        pass
    
    def reverseBitsWithoutBitwise(self, n: int) -> int:
        binary_str = f"{n:032b}"
        reversed_text  = binary_str[::-1]
        return int(reversed_text, 2)