/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) {
            return {};
        } else {
            vector<int> left = rightSideView(root->left);
            vector<int> right = rightSideView(root->right);
            vector<int> ret = {root->val};
            ret.insert(ret.end(), right.begin(), right.end());
            for(int i = right.size(); i < left.size(); i++) {
                ret.push_back(left[i]);
            }
            return ret;
        }
    }
};
