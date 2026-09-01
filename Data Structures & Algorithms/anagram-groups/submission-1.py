class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_lst = defaultdict(list)
        for i in strs:
            sort_str = ''.join(sorted(i)) 
            new_lst[sort_str].append(i)
        return list(new_lst.values())