# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arrList1 = []
        arrList2 = []
        
        if not list1 and not list2:
            return None

        while list1:
            arrList1.append(list1.val)
            list1 = list1.next

        while list2:
            arrList2.append(list2.val)
            list2 = list2.next

        sortedArr = sorted(arrList1+arrList2)

        newLinkedList = None
        for i in range(len(sortedArr) - 1, -1, -1):
            newLinkedList = ListNode(sortedArr[i], newLinkedList)

        return newLinkedList