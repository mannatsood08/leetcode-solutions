# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chc_set = set()
        while head:
            if id(head) in chc_set:
                return head
            chc_set.add(id(head))
            head = head.next
        return None