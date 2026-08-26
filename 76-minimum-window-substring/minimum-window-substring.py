class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        required = len(t)
        best_start = 0
        best_length = float("inf")

        for right in range(len(s)):
            char = s[right]

            if char in need:
                if need[char] > 0:
                    required -= 1
                need[char] -= 1

            while required == 0:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_start = left

                left_char = s[left]

                if left_char in need:
                    need[left_char] += 1

                    if need[left_char] > 0:
                        required += 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]