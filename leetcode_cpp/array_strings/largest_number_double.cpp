#include <iostream>
#include "vector"

using namespace std;

int dominantIndex(vector<int>& nums) {
        int max_1 = -1;
        int max_2 = -1;
        int index = -1;

        for (int i = 0; i < nums.size(); i++) {
            if (max_1 < nums[i]) {
                max_2 = max_1;
                max_1 = nums[i];
                index = i;
            } else if (max_2 < nums[i]) {
                max_2 = nums[i];
            }
        }

        return (max_1 >= max_2*2) ? index : -1;
}

int main(int argc, const char * argv[]) {
    vector<int> nums {1, 2, 3, 4};
    cout << "Result: " << dominantIndex(nums) << endl;
    return 0;
}
