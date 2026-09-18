class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            lst = anagramDict.get(sorted_string)
            if not lst:
                lst = []
            lst.append(string)
            anagramDict[sorted_string] = lst
        
        out = []
        for key, value in anagramDict.items():
            out.append(value)
        
        return out
