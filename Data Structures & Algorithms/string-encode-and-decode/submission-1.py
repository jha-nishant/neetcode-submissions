class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        res = ",".join(sizes)
        res = res + "#"
        strsAppended = "".join(strs)
        res = res + strsAppended
        return res


    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []
        index_of_delimiter = s.find("#")
        encoded_part = s[:index_of_delimiter]
        print(encoded_part)
        sizes = encoded_part.split(",")
        print(sizes)
        out = []
        current_index = index_of_delimiter + 1
        for size in sizes:
            # as current_index is the starting. current_str_end become the start of the next one, then only we will get whole word
            current_str_end = current_index + int(size)
            current_str = s[current_index: current_str_end]
            current_index = current_str_end
            out.append(current_str)
        return out

