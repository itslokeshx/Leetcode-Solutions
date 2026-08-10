class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=""
        min_len=min(len(word) for word in strs)
        flag=True
        for i in range(0,min_len):
            refer=strs[0][i]
            for k in range(0,len(strs)):
                if(strs[k][i]!=refer):
                    flag=False
                    break
            if(flag):
                common+=refer
        return(common)

        