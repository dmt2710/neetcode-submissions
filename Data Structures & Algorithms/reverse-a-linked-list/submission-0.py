# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        arrOfLinkedList = []
        while head:
            arrOfLinkedList.append(head.val)
            head = head.next
        
        newLinkedList = None
        for i in range(len(arrOfLinkedList)):
            newLinkedList = ListNode(arrOfLinkedList[i], newLinkedList)

        return newLinkedList
