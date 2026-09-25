class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            new_num = 0
            if i == len(digits) - 1:
                new_num = num + 1
            else:
                new_num = num + carry
            
            carry = int(new_num / 10)
            val = new_num % 10
            digits[i] = val

            if not carry:
                break
        
        if carry:
            digits.insert(0, 1)
        return digits



        