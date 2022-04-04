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

vector<int> replaceElements(vector<int>& arr) {
    int sz = (int)arr.size();
    int max_so_far = -1;

    for (int i = sz-1; i >= 0; i--) {
        int temp = arr[i];
        arr[i] = max_so_far;

        max_so_far = (max_so_far < temp) ? temp : max_so_far;
    }

    return arr;
}

int main(int argc, const char * argv[]) {

    vector<int> arr {};
    vector<int> result =  replaceElements(arr);

    for (int x : result) {
        cout << x << ",";
    }

    cout << endl;
    return 0;
}
