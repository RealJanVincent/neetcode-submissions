class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> freq = {};
        for (int n : nums) {
            if (freq[n]++) {
                return n;
            }
        }
        return -1;
    }
};
