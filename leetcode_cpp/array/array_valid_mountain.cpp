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

bool validMountainArray(const vector<int>& A) {
    if (A.size() <= 2) return false;

    int sz = (int)A.size();
    int i = 0;

    while (i < sz-1 && A[i] < A[i+1]) i++;

    if (i == 0 || i == sz-1) return false;

    while (i < sz-1 && A[i] > A[i+1]) i++;

    if (i == sz-1) return true;

    return false;
}

int main(int argc, const char * argv[]) {

    vector<int> arr {0,3,2,1};
    cout << validMountainArray(arr) << endl;
    return 0;
}
