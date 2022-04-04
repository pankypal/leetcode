class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_so_far = 0;
        int max = 0;

        for (int i : nums) {
            if (i == 1) {
                max_so_far++;
            } else {
                max = (max < max_so_far) ? max_so_far : max;
                max_so_far = 0;
            }
        }
        
        return (max < max_so_far) ? max_so_far : max;
    }
};
