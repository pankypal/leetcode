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

vector<int> findDisappearedNumbers(vector<int>& nums)
{
    vector<int> res;

    for (int i = 0; i < nums.size(); i++) {
        int index = abs(nums[i]);
        if (nums[index-1] > 0) {
            nums[index-1] = -nums[index-1];
        }
    }

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 0) {
            res.push_back(i+1);
        }
    }

    return res;
}

int main(int argc, const char * argv[]) {

    vector<int> input {4,3,2,7,8,2,3,1};

    vector<int> res = findDisappearedNumbers(input);

    for(auto r : res) {
        cout << r << ",";
    }
    cout << endl;

    return 0;
}
