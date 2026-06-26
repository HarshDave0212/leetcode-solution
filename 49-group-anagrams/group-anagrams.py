from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        temp = ""
        output = []
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            d[temp].append(strs[i])
        for i in d.values():
            output.append(i)
        return output