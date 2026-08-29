class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(word + "~anurag~" for word in strs)

    def decode(self, s: str) -> List[str]:
        return s.split("~anurag~")[:-1]
