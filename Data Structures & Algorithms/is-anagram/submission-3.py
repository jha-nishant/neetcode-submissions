class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        for chr in s:
            chrCount = sDict.get(chr)
            if not chrCount:
                chrCount = 0
            sDict[chr] = chrCount + 1
        print(sDict)
        tDict = {}
        for chr in t:
            chrCount = tDict.get(chr)
            if not chrCount:
                chrCount = 0
            tDict[chr] = chrCount + 1
        print(tDict)
        break_mid_way = False
        for key, value in sDict.items():
            if tDict.get(key) == value:
                del tDict[key]
            else:
                break_mid_way = True
        
        # You will break midway when one of the key doesnt map with the size in other
        if break_mid_way:
            return False
        
        # If you dont break s clears everything it has from t. Still we could have t having some extra chars and so a few keys could be left still.
        return len(tDict.keys()) == 0

        




        