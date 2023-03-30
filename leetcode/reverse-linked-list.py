# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = new_list
            new_list = curr
            curr = next_node
        return new_list