/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* findNextUtil(Node* root, Node* parent)
    {
        if (parent == nullptr)
            return nullptr;
        
        if (root == parent->left && parent->right) {
                return parent->right;
        }
            
        Node* curr = parent->next;
        Node* next = nullptr;
        while (curr != nullptr) {
            if (curr->left != nullptr) {
                next = curr->left;
                break;
            }

            if (curr->right != nullptr) {
                next = curr->right;
                break;
            }

            curr = curr->next;
        }
        return next;
    }
    
    void connectRecurse(Node* root, Node* parent)
    {
        if (root == nullptr)
            return;
        
        root->next = findNextUtil(root, parent);
        
        connectRecurse(root->right, root);
        connectRecurse(root->left, root);
    }
    
    Node* connect(Node* root) {
        connectRecurse(root, nullptr);
        return root;
    }
};
