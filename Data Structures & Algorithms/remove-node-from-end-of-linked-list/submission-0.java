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
        int c = 0;
        ListNode start = head;
        while(head != null){
            head = head.next;
            c++;
        }
        int i = c - n;
        head = start;
        
        ListNode prev = null;
        for(int j = 0; j < i; j++) {
            prev = head;
            head = head.next;
        }
        if(prev == null) {
            return start.next;
        } else {
            prev.next = head.next;
            return start;
        }
    }
}
