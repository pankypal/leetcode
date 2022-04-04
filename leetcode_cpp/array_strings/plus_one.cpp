#include <iostream>
#include "vector"

using namespace std;

vector<int> plusOne(vector<int>& digits) {
        vector<int> res;
        int sum = 1;
        int carry = 0;

        for (int i = digits.size()-1; i >= 0; i--) {
            sum += digits[i];
            sum += carry;
            carry = sum/10;
            res.push_back(sum%10);
            sum = 0;
        }
        
        if (carry > 0) {
            res.push_back(carry);
        }

        reverse(res.begin(), res.end());
        return res;
}

int main(int argc, const char * argv[]) {
    vector<int> nums {1, 2, 3, 4};
    vector<int> res = plusOne(nums);
    for (int n : res) {
        cout << n << ",";
    }
    cout << endl;
    return 0;
}
