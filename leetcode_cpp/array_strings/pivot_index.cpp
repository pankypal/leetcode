#include <iostream>
#include "vector"

using namespace std;

int pivotIndex(vector<int>& nums) {
        int sz = nums.size();
        int leftSum = 0;
        int rightSum = 0;
        
        for (int n : nums) {
            rightSum += n;
        }
        
        for (int i = 0; i < sz; i++) {
            
            rightSum -= nums[i];
            cout << leftSum << endl;
            cout << rightSum << endl;
            if (leftSum == rightSum)
                return i;
            
            leftSum += nums[i];
        }
        
        return -1;
}

int main(int argc, const char * argv[]) {
    vector<int> nums {1,7,3,6,5,6};
    cout << "Result: " << pivotIndex(nums) << endl;
    return 0;
}
