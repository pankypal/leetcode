//
//  main.cpp
//  leetcode
//
//  Created by pankaj pal on 23/06/20.
//  Copyright © 2020 pankaj pal. All rights reserved.
//

#include <iostream>
#include "vector"
#include "set"

using namespace std;

int thirdMax(vector<int>& nums) {
    long max_1 = LONG_MIN;
    long max_2 = LONG_MIN;
    long max_3 = LONG_MIN;

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == max_1 || nums[i] == max_2 || nums[i] == max_3) {
            continue;
        }

        if (nums[i] > max_1) {
            max_3 = max_2;
            max_2 = max_1;
            max_1 = nums[i];
        } else if (nums[i] > max_2) {
            max_3 = max_2;
            max_2 = nums[i];
        } else if (nums[i] > max_3) {
            max_3 = nums[i];
        }
    }

    return max_3 != LONG_MIN ? max_3 : max_1;
}

int main(int argc, const char * argv[]) {

    vector<int> input {3,1};

    cout << "Result: " << thirdMax(input) << endl;
    return 0;
}
