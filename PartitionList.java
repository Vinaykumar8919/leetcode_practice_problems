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
    public ListNode partition(ListNode head, int x) {
        if(head==null || head.next==null) {
            return head;
        }
        ListNode lessx = new ListNode();
        ListNode greater = new ListNode();
        ListNode res =  lessx;
        ListNode sec = greater;
        while(head!=null) {
            if(head.val<x) {
                lessx.next = new ListNode(head.val);
                lessx=lessx.next;
            } else {
                greater.next = new ListNode(head.val);
                greater=greater.next;
            }
            head=head.next;
        }
        lessx.next=sec.next;
        return res.next;  
    }
}
