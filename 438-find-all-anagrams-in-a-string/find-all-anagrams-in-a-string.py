class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        freq_map={}
        p_freq={}
        index_arr=[]
        for char in p:
            if(char not in p_freq):
                p_freq[char]=1
            else:
                p_freq[char]+=1
        for right in range(0,len(s)):
            if(s[right] not in freq_map):
                freq_map[s[right]]=1
            else:
                freq_map[s[right]]+=1
            if(right-left+1==len(p)):
                if(p_freq==freq_map):
                    index_arr.append(left)
                    freq_map[s[left]]-=1
                    if(freq_map[s[left]] == 0):
                        del freq_map[s[left]] 
                    left+=1
                else:
                    freq_map[s[left]]-=1
                    if(freq_map[s[left]] == 0):
                        del freq_map[s[left]] 
                    left+=1
        return index_arr
                    




        