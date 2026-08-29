class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        curr_start, max_end = 0, -1
        res = []
        hash_map = {}

        for char in 'abcdefghijklmnopqrstuvwxyz':
            j = len(s)-1
            while j>=0 and s[j] != char:
                j-=1
            hash_map[char] = j

        for i in range(len(s)):
            if i>max_end:
                if i-curr_start:
                    res.append(i-curr_start)
                curr_start = i
            max_end = max(max_end, hash_map[s[i]])

        res.append(len(s)-curr_start)
        return res        