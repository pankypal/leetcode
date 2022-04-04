//
//  main.cpp
//  practice
//
//  Created by pankaj pal on 11/01/20.
//  Copyright © 2020 pankaj pal. All rights reserved.
//

#include <iostream>
#include <stack>
#include <vector>
#include <queue>

using namespace std;

class BinaryTree {

private:
    struct Node {
        int data;
        struct Node* left;
        struct Node* right;

        Node(int data)
        {
            this->data = data;
            left = nullptr;
            right = nullptr;
        }
    };
    Node* root = nullptr;

    Node* Insert(Node* root, int data)
    {
        if (!root)
        {
            return new Node(data);
        }

        if (root->data > data)
            root->left = Insert(root->left, data);
        else
            root->right = Insert(root->right, data);

        return root;
    }

    void InorderRecursive(Node* root)
    {
        if (root) {
            InorderRecursive(root->left);
            cout << root->data << ",";
            InorderRecursive(root->right);
        }
    }

    void PreorderRecursive(Node* root)
    {
        if (root) {
            cout << root->data << ",";
            PreorderRecursive(root->left);
            PreorderRecursive(root->right);
        }
    }

    void PostorderRecursive(Node* root)
    {
        if (root) {
            PostorderRecursive(root->left);
            PostorderRecursive(root->right);
            cout << root->data << ",";
        }
    }

    void Inorder(Node *root)
    {
        stack<Node*> st;

        if (root == nullptr)
        {
            return;
        }

        while (root || !st.empty())
        {
            while(root)
            {
                st.push(root);

                root = root->left;
            }

            if (!st.empty())
            {
                root = st.top();
                st.pop();
            }

            cout << root->data << ",";

            root = root->right;
        }
    }

    void Preorder(Node* root)
    {
        stack<Node*> st;

        if (root == nullptr)
        {
            return;
        }

        while (root || !st.empty())
        {
            while (root)
            {
                cout << root->data << ",";

                if (root->right)
                {
                    st.push(root->right);
                }

                root = root->left;
            }

            if (!st.empty())
            {
                root = st.top();
                st.pop();
            }
        }
    }

    void Postorder(Node* root)
    {
        stack<Node*> st;
        stack<Node*> result;

        if (root == nullptr)
        {
            return;
        }

        st.push(root);

        while (!st.empty())
        {
            auto temp = st.top();
            st.pop();

            result.push(temp);

            if (temp->left)
            {
                st.push(temp->left);
            }

            if (temp->right)
            {
                st.push(temp->right);
            }
        }

        while(!result.empty())
        {
            cout << result.top()->data << ",";
            result.pop();
        }
    }

    void Postorder1(Node* root)
    {
        stack<Node*> st;

        if (root == nullptr)
        {
            return;
        }

        st.push(root);

        while(!st.empty())
        {
            Node* temp = st.top();

            bool doneSubtrees = (root == temp->left || root == temp->right);
            bool isLeaf = (temp->left == nullptr && temp->right == nullptr);

            if (doneSubtrees || isLeaf)
            {
                st.pop();
                cout << temp->data << ",";
                root = temp;
            }
            else
            {
                if (temp->right)
                {
                    st.push(temp->right);
                }
                if (temp->left)
                {
                    st.push(temp->left);
                }
            }
        }
    }

    vector<vector<int>> LevelOrder(Node* root)
    {
        vector<vector<int>> result;

        if (root == nullptr)
        {
            return result;
        }

        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            int n = (int)q.size();

            vector<int> v;
            while (n > 0) {
                auto node = q.front();
                q.pop();

                v.push_back(node->data);

                if (node->left)
                    q.push(node->left);

                if (node->right)
                    q.push(node->right);

                n--;
            }

            result.push_back(v);
        }

        return result;
    }

    int MaxDepthRec(Node* root)
    {
        if (root == nullptr)
        {
            return 0;
        }

        int left = MaxDepthRec(root->left);
        int right = MaxDepthRec(root->right);

        return (left > right) ? left+1 : right + 1;
    }

    Node* LCA(Node* root, Node* p, Node* q)
    {
        if (root == nullptr)
            return nullptr;

        if (root == p || root == q)
            return root;

        Node* left_lca = LCA(root->left, p, q);
        Node* right_lca = LCA(root->right, p, q);

        if (left_lca && right_lca)
            return root;

        return (left_lca != nullptr) ? left_lca : right_lca;
    }

    int findUtil(vector<int>& arr, int val)
    {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == val)
                return i;
        }

        return -1;
    }

public:
    void Insert(int data)
    {
        root = Insert(root, data);
    }

    void InorderRecursive()
    {
        cout<<"Inorder Traversal: ";
        InorderRecursive(root);
        cout<<endl;
    }

    void Inorder()
    {
        cout<<"InOrder Non-rec: ";
        Inorder(root);
        cout << endl;
    }

    void PreorderRecursive()
    {
        cout<<"Preorder Traversal: ";
        PreorderRecursive(root);
        cout<<endl;
    }

    void Preorder()
    {
        cout << "Preorder Non-rec: ";
        Preorder(root);
        cout << endl;
    }

    void PostorderRecursive()
    {
        cout<<"Postorder Traversal: ";
        PostorderRecursive(root);
        cout<<endl;
    }

    void Postorder()
    {
        cout << "Postorder Non-rec: ";
        //Postorder(root);
        Postorder1(root);
        cout << endl;
    }

    void LevelOrderTraversal()
    {
        cout << "Level order traversal: ";
        auto res = LevelOrder(root);

        for (auto r : res) {
            cout <<endl;
            for (auto c : r) {
                cout << c << ",";
            }
        }
        cout << endl;
    }

    void MaxDepth()
    {
        cout << "Max depth: " << MaxDepthRec(root) << endl;
    }

    bool isMirror(Node* left, Node* right)
    {
        if (left == nullptr && right == nullptr)
            return true;

        if (left == nullptr || right == nullptr)
            return false;

        if (left->data != right->data)
            return false;

        return isMirror(left->left, right->right) && isMirror(left->right, right->left);
    }

    bool isSymmetric(Node* root) {
        if (root == nullptr)
            return true;

        return isMirror(root->left, root->right);
    }

    bool hasPathSum(Node* root, int targetSum) {
        if (root == nullptr)
            return false;

        targetSum -= root->data;

        if (root->left == nullptr && root->right == nullptr) {
            return targetSum == 0;
        }

        return hasPathSum(root->left, targetSum)
            || hasPathSum(root->right, targetSum);
    }

    Node* BuildTreeFromInAndPre(vector<int>& preorder, vector<int>& inorder, int start, int end, int& pre_start)
    {
        if (start > end)
            return nullptr;

        Node* node = new Node(preorder[pre_start]);
        pre_start++;

        if (start == end)
            return node;

        int index = findUtil(inorder, node->data);

        if (index != -1) {
            node->left = BuildTreeFromInAndPre(preorder, inorder, start, index-1, pre_start);
            node->right = BuildTreeFromInAndPre(preorder, inorder, index+1, end, pre_start);
        }

        return node;
    }

    void BuildTreeFromInAndPre(vector<int>& preorder, vector<int>& inorder)
    {
        cout<<"Building tree from inorder and preorder input: ";
        int pre_start = 0;
        Node* node = BuildTreeFromInAndPre(preorder, inorder, 0, (int)inorder.size()-1, pre_start);
        InorderRecursive(node);
        cout << endl;
    }

    Node* BuildTreeFromInAndPost(vector<int>& inorder, vector<int>& postorder, int start, int end, int& post_end)
    {
        if (start > end)
            return nullptr;

        Node* node = new Node(postorder[post_end]);
        post_end--;

        if (start == end)
            return node;

        int index = findUtil(inorder, node->data);

        if (index != -1) {
            node->right = BuildTreeFromInAndPost(inorder, postorder, index+1, end, post_end);
            node->left = BuildTreeFromInAndPost(inorder, postorder, start, index-1, post_end);
        }

        return node;
    }

    void BuildTreeFromInAndPost(vector<int>& inorder, vector<int>& postorder)
    {
        cout<<"Building tree from inorder and postorder input: ";
        int post_end = (int)postorder.size()-1;
        Node* node = BuildTreeFromInAndPost(inorder, postorder, 0, (int)inorder.size()-1, post_end);
        InorderRecursive(node);
        cout<<endl;
    }
};


int main(int argc, const char * argv[])
{
    BinaryTree tree;

    tree.Insert(15);
    tree.Insert(20);
    tree.Insert(5);
    tree.Insert(13);
    tree.Insert(25);
    tree.Insert(3);

    tree.InorderRecursive();
    tree.Inorder();

    tree.PreorderRecursive();
    tree.Preorder();

    tree.PostorderRecursive();
    tree.Postorder();

    tree.LevelOrderTraversal();

    tree.MaxDepth();

    vector<int> inorder {9,3,15,20,7};
    vector<int> preorder {3,9,20,15,7};
    tree.BuildTreeFromInAndPre(preorder, inorder);

    vector<int> postorder {9,15,7,20,3};
    tree.BuildTreeFromInAndPost(inorder, postorder);


    return 0;
}
