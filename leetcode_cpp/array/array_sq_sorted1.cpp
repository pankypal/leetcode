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

vector<int> sortedSquares(vector<int>& nums) {
    vector<int> res;

    int i = 0;
    int j = nums.size()-1;

    if (j<0) {
        return res;
    }

    while (i <= j) {
        if (nums[i]*nums[i] >= nums[j]*nums[j]) {
            res.push_back(nums[i]*nums[i]);
            i++;
        } else {
            res.push_back(nums[j]*nums[j]);
            j--;
        }
    }

    reverse(res.begin(), res.end());


    return res;
}

int main(int argc, const char * argv[]) {

    vector<int> input {-7,-3,2,3,11};

    vector<int> res = sortedSquares(input);

    for(auto r : res) {
        cout << r << ",";
    }
    cout << endl;

    return 0;
}
