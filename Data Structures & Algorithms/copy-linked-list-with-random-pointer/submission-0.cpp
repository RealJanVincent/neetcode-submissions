/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return nullptr;
        }

        std::unordered_map<Node*, Node*> nodes;

        Node* new_head = new Node(head->val);
        nodes[head] = new_head;

        // if (head->next != nullptr && !nodes.count(head->next)) {
        //     nodes[head->next] = new Node(head->next->val);
        // } else {
        //     nodes[head->next] = nullptr;
        // }
        // new_head->next = nodes[head->next];

        // if (head->random != nullptr && !nodes.count(head->random)) {
        //     nodes[head->random] = new Node(head->random->val);
        
        // } else {
        //     nodes[head->random] = nullptr;
        // }
        // new_head->random = nodes[head->random];

        while (head != nullptr) {
            if (head->next != nullptr && !nodes.count(head->next)) {
                nodes[head->next] = new Node(head->next->val);
            } else if (head->next == nullptr){
                nodes[head->next] = nullptr;
            }
            nodes[head]->next = nodes[head->next];

            if (head->random != nullptr && !nodes.count(head->random)) {
                nodes[head->random] = new Node(head->random->val);
            } else if (head->random == nullptr){
                nodes[head->random] = nullptr;
            }
            nodes[head]->random = nodes[head->random];
            
            head = head->next;
        }
        return new_head;
    }
};
