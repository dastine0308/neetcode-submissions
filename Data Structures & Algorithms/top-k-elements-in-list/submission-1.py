from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k_items = counts.most_common(k)
        return [item[0] for item in top_k_items]