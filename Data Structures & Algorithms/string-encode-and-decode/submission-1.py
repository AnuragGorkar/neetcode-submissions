class Solution:
    def encode(self, strs: List[str]) -> str:
        print("".join(f"{len(word)}#{word}" for word in strs))
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find #
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
        return res
