class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            ## c is part of solution
            c = s[i]
            count = charDict.get(c)
            if count == None:
                count = 0
            count += 1

            charDict[c] = count
            
            max_char_count = 0
            for key, value in charDict.items():
                max_char_count = max(max_char_count, value)


            while i + 1 - max_char_count - start > k:
                # retreat from start
                start_c = s[start]
                count_start = charDict.get(start_c)
                count_start -= 1
                if count_start == 0:
                    del charDict[start_c]
                else:
                    charDict[start_c] = count_start
                start += 1
            max_len = max(max_len, i + 1 - start)
            
        
        return max_len

