class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heap = [-c for c in citations]
        heapq.heapify(heap)
        result = 0
        while heap and result < -heap[0]:
            heapq.heappop(heap)
            result += 1
        
        return result