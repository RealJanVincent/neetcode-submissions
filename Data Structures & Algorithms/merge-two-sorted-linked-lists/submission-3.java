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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        } else {
            ListNode big = list1;
            ListNode small = list2;
            if (big.val < small.val) {
                ListNode temp = big;
                big = small;
                small = temp;
            }
            ListNode rec = mergeTwoLists(big, small.next);
            return new ListNode(small.val, rec);
        }
    }
}