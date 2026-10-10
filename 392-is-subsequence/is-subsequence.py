class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        source_pointer = 0
        target_pointer = 0

        if s == "":
            return True

        for index in range(len(t)):
            if s[source_pointer] == t[target_pointer]:
                source_pointer += 1
                target_pointer += 1
            else:
                target_pointer += 1

            if source_pointer == len(s):
                return True

        return False