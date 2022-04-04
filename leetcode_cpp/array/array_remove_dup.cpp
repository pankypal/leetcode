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
    vector<int> nums {0};
    int i = 0;
    int j = 0;

    if (nums.size() <= 1) {
        cout << nums.size() << endl;
        return (int)nums.size();
    }

    i = 1;
    for (;i < nums.size() && j < nums.size(); i++) {
        if (nums[i] == nums[j]) {
            continue;
        }

        nums[++j] = nums[i];
    }

    for (int n : nums)
        cout<<n<<",";

    cout <<endl;

    cout << j << endl;

    return 0;
}
