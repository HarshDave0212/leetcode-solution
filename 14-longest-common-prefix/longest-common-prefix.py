class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ch = strs[0]
        for i in strs:
            x = min(len(i), len(ch))
            ch = ch[:x]
            for j in range(x):
                
                if i[j] != ch[j]:
                    
                    ch = ch[:j]
                    break
        return ch