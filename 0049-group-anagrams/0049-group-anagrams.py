class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in range(0,len(strs)):
            sortedstr="".join(sorted(strs[i]))
            if(sortedstr not in group):
                group[sortedstr]=[strs[i]]
            else:
                group[sortedstr].append(strs[i])
        return(list(group.values()))
        