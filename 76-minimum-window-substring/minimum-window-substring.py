class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        t_freq = {}
        window_freq = {}
        window = ""

        for char in t:
            if char not in t_freq:
                t_freq[char] = 1
            else:
                t_freq[char] += 1

        for right in range(len(s)):

            if s[right] not in window_freq:
                window_freq[s[right]] = 1
            else:
                window_freq[s[right]] += 1

            if right - left + 1 >= len(t):

                flag = True

                for char, freq_count in t_freq.items():
                    if window_freq.get(char, 0) < freq_count:
                        flag = False
                        break

                while flag:

                    if len(window) == 0:
                        window = s[left:right + 1]
                    elif len(window) > right - left + 1:
                        window = s[left:right + 1]

                    window_freq[s[left]] -= 1

                    if window_freq[s[left]] == 0:
                        del window_freq[s[left]]

                    left += 1

                    flag = True

                    for char, freq_count in t_freq.items():
                        if window_freq.get(char, 0) < freq_count:
                            flag = False
                            break

        return window