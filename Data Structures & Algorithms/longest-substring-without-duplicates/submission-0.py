class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        start_index = -1 # last occurence
        max_length = 0
        for index in range(len(s)):
            #index is the last index
            ch = s[index]
            if ch in charDict:
                start_index = max(charDict[ch], start_index)
            charDict[ch] = index
            current_length = index - start_index
            max_length = max(max_length, current_length)
        return max_length
