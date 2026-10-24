class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        if len(counts) == 1:
            return [nums[0]]
        
        arr = []
        for count, freq in counts.items():
            arr.append((freq, count))
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        return result
        

        