# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
        slow = head 
        fast = head 
        prev = None

        while fast and fast.next:
            prev = slow 
            fast = fast.next.next
            slow = slow.next 
            # print(fast.val, slow.val)

        prev.next = slow.next
        return head