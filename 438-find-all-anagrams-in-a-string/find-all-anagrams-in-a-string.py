class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        window_freq = {}
        pattern_freq = {}
        result = []

        for char in p:
            if char not in pattern_freq:
                pattern_freq[char] = 1
            else:
                pattern_freq[char] += 1

        for right in range(len(s)):
            if s[right] not in window_freq:
                window_freq[s[right]] = 1
            else:
                window_freq[s[right]] += 1

            if right - left + 1 == len(p):
                if pattern_freq == window_freq:
                    result.append(left)

                window_freq[s[left]] -= 1

                if window_freq[s[left]] == 0:
                    del window_freq[s[left]]

                left += 1

        return result