class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> freq(3);
        for (int n : nums) {
            freq[n]++;
        }
        for (int i = 0, j = 0; i < nums.size(); i++) {
            while (freq[j] == 0) {
                j++;
            }
            nums[i] = j;
            freq[j]--;
        }
    }
};