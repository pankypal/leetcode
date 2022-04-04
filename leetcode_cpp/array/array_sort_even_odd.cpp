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

vector<int> sortArrayByParity(vector<int>& A) {
    int sz = (int)A.size();
    int i = 0, j = sz-1;

    while (i < j) {
        if (A[i]%2 != 0) {
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            j--;
        } else {
            i++;
        }
    }

    return A;
}

int main(int argc, const char * argv[]) {

    vector<int> arr {2,2,4,6};
    vector<int> result = sortArrayByParity(arr);

    for (int x : arr) {
        cout << x << ",";
    }

    cout << endl;
    return 0;
}
