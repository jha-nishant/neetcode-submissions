class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. reverse string
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

        # 2. Two pointer
        result = True
        left = 0
        right = len(s) - 1
        while right > left:
            left_char = s[left]
            if not left_char.isalnum():
                left = left + 1
                continue
            
            right_char = s[right]
            if not right_char.isalnum():
                right = right - 1
                continue
            
            # now that we have alphanumeric on both sides
            print(f"left: {left_char}, right: {right_char}")
            if left_char.lower() == right_char.lower():
                left = left + 1
                right = right - 1
            else:
                result = False
                break
        
        return result

