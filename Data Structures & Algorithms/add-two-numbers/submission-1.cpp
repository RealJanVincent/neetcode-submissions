/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(0);

        ListNode* cur = res;
        int carry = 0;
        int sum = 0;
        int l2_val = 0;
        while (l1 != nullptr || l2 != nullptr) {
            if (l1 == nullptr) {
                l1 = l2; 
                l2 = nullptr;
            }
            l2_val = l2 == nullptr ? 0 : l2->val;
            sum = l1->val + l2_val + carry;
            cur->val = sum % 10;

            carry = sum >= 10 ? 1 : 0;
            l1 = l1->next;
            l2 = l2 == nullptr ? nullptr : l2->next;
            if (l1 != nullptr || l2 != nullptr) {
                cur->next = new ListNode();
                cur = cur->next;
            }
        }

        if (carry != 0) {
            cur->next = new ListNode(carry);
        }

        return res;
    }
};
