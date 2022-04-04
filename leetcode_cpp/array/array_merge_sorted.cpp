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
    vector<int> nums1 {1,2,3};
    vector<int> nums2 {};

    int m = 3;
    int n = 0;
    vector<int> res;
    int destination = m+n-1;
    int i = m-1;
    int j = n-1;

    while (i >=0 && j >= 0){
        if (nums1[i] > nums2[j]) {
            nums1[destination--] = nums1[i--];
        } else {
            nums1[destination--] = nums2[j--];
        }
    }

    while (i >= 0){
        nums1[destination--] = nums1[i--];
    }

    while (j >= 0) {
        nums1[destination--] = nums2[j--];
    }

    for (int n : nums1)
        cout<<n<<",";

    cout <<endl;

    return 0;
}
