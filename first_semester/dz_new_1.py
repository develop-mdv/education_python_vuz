# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        while l1 is not None and l2 is not None:
            if l1.next is not None and l2.next is not None:
                cur.next = ListNode(val=(cur.val+l1.val + l2.val) // 10)
            elif (cur.val+l1.val + l2.val) // 10:
                cur.next = ListNode(val=(cur.val+l1.val + l2.val) // 10)
            cur.val = (cur.val + l1.val + l2.val) % 10
            l1 = l1.next
            l2 = l2.next
            if l1 is not None and l2 is not None:
                cur = cur.next

        if l1 is not None:
            ost = l1
        elif l2 is not None:
            ost = l2
        else:
            ost = None
        if cur.next is None and ost is not None:
            cur.next = ListNode()
        while ost is not None:
            cur = cur.next
            if ost.next is not None:
                cur.next = ListNode(val=(cur.val + ost.val) // 10)
            elif (cur.val + ost.val) // 10:
                cur.next = ListNode(val=(cur.val + ost.val) // 10)
            cur.val = (cur.val + ost.val) % 10
            ost = ost.next
        return ans
