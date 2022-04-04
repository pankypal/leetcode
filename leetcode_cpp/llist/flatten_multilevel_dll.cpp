/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flattenRec(Node* head) {
        if (head == nullptr)
            return head;
        
        if (head->child == nullptr) {
            if (head->next == nullptr) {
                return head;
            } else {
                return flattenRec(head->next);
            }
        } else {
            Node* child = head->child;
            head->child = nullptr; // w/o this submission fails as it is invalid DLL
            Node* next = head->next;
            
            Node* lastChild = flattenRec(child);
            head->next = child;
            child->prev = head;
            
            if (next != nullptr) {
                lastChild->next = next;
                next->prev = lastChild;
                
                return flattenRec(next);
            }
            
            return lastChild;
        }
    }
    
    Node* flatten(Node* head) {
        flattenRec(head);
        
        return head;
    }
};
