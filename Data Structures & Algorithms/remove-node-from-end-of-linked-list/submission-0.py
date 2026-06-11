# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list_head = []
        
        while curr:
            list_head.append(curr)
            curr = curr.next

        remove_idx = len(list_head) - n

        if remove_idx == 0:
            return head.next

        
        pre_node =  list_head[remove_idx - 1]
        pre_node.next = list_head[remove_idx].next

        return head




            