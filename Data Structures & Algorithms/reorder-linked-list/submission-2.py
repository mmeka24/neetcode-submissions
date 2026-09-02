# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        # have a slow and fast pointer and replace the fast and slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # atp slow is at first half and fast is at end 
        
        second = slow.next
        slow.next = None
        prev = None
        
        # reversing second portion of list
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        # merge the two halves of the list 

        second = prev
        first = head

        while second:
            temp1 = second.next
            temp2 = first.next
            first.next = second
            second.next = temp2
            first = temp2
            second = temp1

        



        