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

void moveZeroes(vector<int>& nums) {
    int sz = (int)nums.size();

    int i = 0, j = 0;

    for (; i < sz;) {
        if (nums[i] == 0) {
            i++;
        } else {
            nums[j++] = nums[i++];
        }
    }

    while (j < sz) {
        nums[j++] = 0;
    }
}

int main(int argc, const char * argv[]) {

    vector<int> arr {0, 0, 1};
    moveZeroes(arr);

    for (int x : arr) {
        cout << x << ",";
    }

    cout << endl;
    return 0;
}
