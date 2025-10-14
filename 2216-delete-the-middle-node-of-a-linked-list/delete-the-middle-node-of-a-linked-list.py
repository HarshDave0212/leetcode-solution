# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
        count = 0 
        temp = head
        while temp:
            temp = temp.next
            count+=1
        mid = count//2
        print(mid)
        temp = head
        for i in range(mid-1):
            temp = temp.next
        temp.next = temp.next.next
        return head