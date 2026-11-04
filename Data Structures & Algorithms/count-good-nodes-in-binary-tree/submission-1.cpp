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
private:
    void dfs(TreeNode* root, int max, int* counter) {
        if (root) {
            if (root->val >= max) {
                (*counter)++;
            }
            max = root->val > max ? root->val : max;
            dfs(root->left, max, counter);
            dfs(root->right, max, counter);
        }
    }

public:
    int goodNodes(TreeNode* root) {
        int res = 0;

        dfs(root, -101, &res);

        return res;
    }
};
