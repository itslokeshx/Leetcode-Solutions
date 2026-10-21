class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in range(len(strs)):
            word="".join(sorted(strs[i]))
            if(word not in freq):
                freq[word]=[strs[i]]
            else:
                freq[word].append(strs[i])
        return list(freq.values())



            


        