class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        if not matrix or not matrix[0]:
            return -1
        heap = []

        for li in matrix:
            for element in li:
                nextVal = -element
                heappush(heap, nextVal)

                if len(heap) > k:
                    heappop(heap)

        return -heap[0] if heap else -1
        