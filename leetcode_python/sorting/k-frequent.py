from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        unique_nums = list(freq.keys())
        minHeap = [(freq[num], num) for num in unique_nums[:k]]
        heapq.heapify(minHeap)

        for num in unique_nums[k:]:
            heapq.heappush(minHeap, (freq[num], num))
            heapq.heappop(minHeap)

        return [el[1] for el in minHeap] # return in any order

    def topKFrequent1(self, nums, k):
        freq = Counter(nums)

        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num, freq in freq.items():
            buckets[freq].append(num)

        res = []
        for bucket in buckets[::-1]:
            if not bucket:
                continue

            for num in bucket:
                if len(res) != k:
                    res.append(num)
                    if len(res) == k:
                        break
            
        return res

        

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent1([1,1,1,2,2,3], 2))