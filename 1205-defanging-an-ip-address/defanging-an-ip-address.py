class Solution:
    def defangIPaddr(self, address: str) -> str:
        op=address.replace(".","[.]")
        return op
        