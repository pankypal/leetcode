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
        if (head == nullptr)
            return nullptr;
        
        Node *curr = head;
        
        while (curr) {
            Node *temp = new Node(curr->val);
            temp->next = curr->next;
            curr->next = temp;
            
            curr = temp->next;
        }
        
        curr = head;
        while (curr) {
            curr->next->random = curr->random ? curr->random->next : nullptr;
            curr = curr->next->next;
        }
        
        curr = head;
        Node *res = head->next;
        
        while (curr) {
            Node *temp = curr->next;
            curr->next = curr->next->next;
            
            if (temp->next)
                temp->next = temp->next->next;
            
            curr = curr->next;
        }
        
        return res;
    }
};
