/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr)
            return "#";
        
        string left = serialize(root->left);
        string right = serialize(root->right);
        
        return to_string(root->val) + "," + left + "," + right;
    }
    
    queue<string> splitData(string data)
    {
        vector<string> arr;
        stringstream ss(data);
        while (ss.good()) {
            string temp;
            getline(ss, temp, ',');
            
            if (!temp.empty()) {
                arr.push_back(temp);
            }
        }
        
        queue<string> q;
        for (auto s : arr) {
            q.push(s);
        }
        
        return q;
    }
    
    TreeNode* _deserialize(queue<string>& q)
    {
        if (q.size() == 0)
            return nullptr;
        
        string temp = q.front();
        q.pop();
        
        if (temp == "#") {
            return nullptr;
        }
        
        TreeNode* root = new TreeNode(stoi(temp));
        root->left = _deserialize(q);
        root->right = _deserialize(q);
        
        return root;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        queue<string> nodes = splitData(data);
        
        return _deserialize(nodes);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
