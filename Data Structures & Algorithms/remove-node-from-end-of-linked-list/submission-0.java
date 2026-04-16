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
        ListNode parent = new ListNode(-1, head);
        int length = 0;
        ListNode temp = head;
        if(head == null) return head;
        while(temp != null) {
            length++;
            temp = temp.next;
        }
        System.out.println(length);
        temp = parent;
        for(int i = 0; i < length - n; i++) {
            temp = temp.next;
        }

        temp.next = temp.next.next;
        return parent.next;
    }
}
