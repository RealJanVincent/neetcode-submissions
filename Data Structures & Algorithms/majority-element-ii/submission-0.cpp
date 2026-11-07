class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int n : nums) {
            freq[n]++;
        }
        int third = nums.size() / 3;
        vector<int> res;
        for (auto it : freq) {
            if (it.second > third) {
                res.push_back(it.first);
            }
        }
        return res;
    }
};