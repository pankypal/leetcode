//
//  main.cpp
//  leetcode
//
//  Created by pankaj pal on 23/06/20.
//  Copyright © 2020 pankaj pal. All rights reserved.
//

#include <iostream>
#include "vector"

using namespace std;

int main(int argc, const char * argv[]) {
    vector<int> nums {3,3,3,3};
    int val = 3;
    int i = 0;
    int j = 0;

    for (;i < nums.size() && j < nums.size(); i++) {
        if (nums[i] != val) {
            nums[j++] = nums[i];
        }
    }

    for (int n : nums)
        cout<<n<<",";

    cout <<endl;

    cout << j << endl;

    return 0;
}
