
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag= True
                break
        fast = head
        while slow!=fast and slow:
            slow=slow.next
            fast=fast.next
        if flag:
            return slow
        else:

            return None
        

        
