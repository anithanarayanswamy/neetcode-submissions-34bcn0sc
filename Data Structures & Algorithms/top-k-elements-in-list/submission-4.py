class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_k = {}
        for i in nums:
            dict_k[i] = 1 + dict_k.get(i, 0)
        
        # Step 2: Group [frequency, element] pairs
        arr = []
        for i, c in dict_k.items():
            arr.append([c, i])
        
        # FIX: Sort ONCE after the loop finishes, in reverse (highest frequency first)
        arr.sort(reverse=True)
        
        # Step 3: Extract the top k elements
        res = []
        for j in range(k):
            res.append(arr[j][1])
            
        return res
        
        