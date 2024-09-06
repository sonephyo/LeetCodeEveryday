# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                return slow

        return slow



            
        