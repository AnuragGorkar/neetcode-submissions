class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        output_dict = defaultdict(list)
        for word in strs:
            count_array = [0] * 26
            for char in word:
                count_array[ord(char)-97] += 1
            ana_hash = "".join(chr(index+97) + str(count) if count>0 else "" for index, count in enumerate(count_array))
            output_dict[ana_hash].append(word) 
        for val in output_dict.values():
            res.append(val)
        return res
        