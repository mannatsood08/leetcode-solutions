class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        dummy = ListNode()
        current = head
        c = dummy
        while current:
            lst.append(current.val)
            current = current.next
        lst.sort()
        for value in lst:
            c.next = ListNode(value)  
            c = c.next  
        return dummy.next