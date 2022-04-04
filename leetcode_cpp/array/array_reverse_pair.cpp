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

int heightChecker(vector<int>& heights) {
    vector<int> temp = heights;
    int result = 0;

    sort(temp.begin(), temp.end());

    for (int i = 0; i < (int)heights.size(); i++) {
        if (heights[i] != temp[i]) {
            result++;
        }
    }

    return result;
}

int main(int argc, const char * argv[]) {

    vector<int> arr {};
    cout << heightChecker(arr) << endl;

    cout << endl;
    return 0;
}
