/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        int count = 0;
        while(temp!=null) {
            count++;
            temp=temp.next;
        }
        count=count-n;
        if(count<=0) {
            return head.next;
        } else {
            temp=head;
            for(int i=1; i<count; i++ ) {
                temp=temp.next;
            }
            temp.next=temp.next.next;
        }
        return head;
        
    }
}
