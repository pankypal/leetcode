//
//  main.cpp
//  leetcode
//
//  Created by pankaj pal on 23/06/20.
//  Copyright © 2020 pankaj pal. All rights reserved.
//

#include <iostream>
#include "vector"
#include "unordered_map"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> values;
        vector<int> res;
        bool found = false;

        for (int i = 0; i < nums.size(); i++) {
            if (values.find(target-nums[i]) != values.end()) {
                res.push_back(values[target-nums[i]]);
                res.push_back(i);
                found = true;
                break;
            }

            values[nums[i]] = i;
        }

        if (!found) {
            res.push_back(-1);
            res.push_back(-1);
        }

        return res;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> inp {2, 7, 11, 15};

    auto res = sol.twoSum(inp, 9);

    cout << res[0] << endl;
    cout << res[1] << endl;
    return 0;
}
