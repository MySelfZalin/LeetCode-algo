# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range (0, len(lists), 2):
                f = lists[i]
                s = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merged_sorted_list(f,s))
            lists = merged_lists
        return lists[0]        


    def merged_sorted_list(self, first, second):
        dummy = ListNode()
        curr = dummy
        while first and second:
            if first.val <= second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next

        curr.next = first if first else second
        return dummy.next    



        

        