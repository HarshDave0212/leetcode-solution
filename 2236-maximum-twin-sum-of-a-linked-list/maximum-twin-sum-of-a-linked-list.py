# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        count_o =[]
        count_e =[]
        maxi = 0
        while fast and fast.next:
            count_o.append(fast.val)
            count_e.append(fast.next.val)
            fast = fast.next.next
        l = len(count_o)
        count_e.reverse()
        for i in range(l):
            summ = count_o[i] + count_e[i]
            maxi = max(maxi, summ)
        return maxi