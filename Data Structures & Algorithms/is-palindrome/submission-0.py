class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. reverse string
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

        # 2. Two pointer
        # left = 0
        # right = len(s)
        # while right > left:

