class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dic = defaultdict(list)
        for i in strs:
            sort_i = ''.join(sorted(i))
            sort_dic[sort_i].append(i)
        return list(sort_dic.values())
        