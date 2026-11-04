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
    public void reorderList(ListNode head) {
        Deque<ListNode> stck = new ArrayDeque<>();
        int c = 0;
        ListNode inOrder = head;
        while(inOrder != null) {
            stck.push(inOrder);
            inOrder = inOrder.next;
            c++;
        }
        inOrder = head;
        for(int i = 0; i < c; i++) {
            if(i == c - 1){
                head.next = null;
            } else if(i % 2 == 0) {
                inOrder = inOrder.next;
                head.next = stck.pop();
                head = head.next;
            } else {
                head.next = inOrder;
                head = head.next;
            }
        }
    }
}
