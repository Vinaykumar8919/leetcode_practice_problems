# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if not headB or not headA:
        #     return headA
        # tempB = headB
        # while headA:
        #     headB = tempB
        #     while headB:
        #         if headA==headB:
        #             return headA
        #         headB=headB.next
        #     headA=headA.next
            
        # setA = set()
        # while headA:
        #     setA.add(headA)
        #     headA=headA.next
        # while headB:
        #     if headB in setA:
        #         return headB
        #     headB=headB.next

        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        while tempA!=tempB:
            if tempA==None:
                tempA=headB
            else:
                tempA=tempA.next
            if tempB==None:
                tempB=headA
            else:
                tempB=tempB.next
        return tempA
