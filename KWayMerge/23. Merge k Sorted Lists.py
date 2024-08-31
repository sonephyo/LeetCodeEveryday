# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        minHeap = []

        for root in lists:
            if root is not None:
                heappush(minHeap, root)

        heapHead, heapTail = None, None

        while minHeap:
            node = heappop(minHeap)
            if heapHead is None:
                heapHead = heapTail = node
            else:
                heapTail.next = node
                heapTail = heapTail.next

            if node.next is not None:
                heappush(minHeap, node.next)

        return heapHead


        