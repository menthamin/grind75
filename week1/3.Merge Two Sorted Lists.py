# https://leetcode.com/problems/merge-two-sorted-lists/
# 참고자료: https://www.youtube.com/watch?v=n7DLmBPpNkY

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        new_list = ListNode(None)
        head = new_list

        while list1 and list2:
            if list1.val > list2.val:
                new_node = ListNode(list2.val)
                list2 = list2.next
            else:
                new_node = ListNode(list1.val)
                list1 = list1.next

            new_list.next = new_node
            new_list = new_list.next

        if list1:
            new_list.next = list1

        if list2:
            new_list.next = list2

        return head.next
