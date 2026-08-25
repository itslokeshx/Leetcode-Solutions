class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_map = {}
        for s in s1:
            if s not in s1_map:
                s1_map[s] = 1
            else:
                s1_map[s] += 1
        flag = False
        s2_map = {}
        for right in range(len(s2)):
            if(s2[right] not in s2_map):
                s2_map[s2[right]] = 1
            else:
                s2_map[s2[right]] += 1
            if(right - left + 1 == len(s1)):
                if(s1_map == s2_map):
                    flag = True
                s2_map[s2[left]] -= 1
                if(s2_map[s2[left]] == 0):
                    del s2_map[s2[left]]
                left += 1
        return flag