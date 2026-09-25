class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverseBitsWithBitwise(n)

    def reverseBitsWithBitwise(self, n: int) -> int:
        # special bitwise logic can be applied
        # Implement that
        # Swap adjacent 16-bit blocks
        n = ((n >> 16) & 0x0000FFFF) | ((n & 0x0000FFFF) << 16)
        # Swap adjacent 8-bit blocks
        n = ((n >> 8) & 0x00FF00FF) | ((n & 0x00FF00FF) << 8)
        # Swap adjacent 4-bit blocks
        n = ((n >> 4) & 0x0F0F0F0F) | ((n & 0x0F0F0F0F) << 4)
        # Swap adjacent 2-bit blocks
        n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2)
        # Swap adjacent 1-bit blocks
        n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1)
        return n
    
    def reverseBitsWithoutBitwise(self, n: int) -> int:
        binary_str = f"{n:032b}"
        reversed_text  = binary_str[::-1]
        return int(reversed_text, 2)