class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Dict = {}
        for c in s1:
            count = s1Dict.get(c)
            if count is None:
                count = 0
            s1Dict[c] = count + 1
        s2Dict = {}
        for i in range(len(s1)):
            c = s2[i]
            count = s2Dict.get(c)
            if count is None:
                count = 0
            s2Dict[c] = count + 1

        if self.isPermutation(s1Dict, s2Dict) == True:
            return True
        out = False
        for i in range(1, len(s2) - len(s1) + 1):
            rem = s2[i - 1]
            add = s2[len(s1) - 1 + i]
            print(rem)
            rem_count = s2Dict.get(rem)
            rem_count -= 1
            if rem_count == 0:
                del s2Dict[rem]
            else:
                s2Dict[rem] = rem_count

            addCount = s2Dict.get(add)
            if addCount == None:
                addCount = 0
            s2Dict[add] = addCount + 1

            if self.isPermutation(s1Dict, s2Dict) == True:
                out = True
                break
        
        return out


            
    
    def isPermutation(self, s1Dict: Dict, s2Dict: Dict) -> bool:
        if len(s1Dict.keys()) != len(s2Dict.keys()):
            return False
        result = True
        for key, value in s1Dict.items():
            s2Value = s2Dict.get(key)
            if value != s2Value:
                result = False
        return result