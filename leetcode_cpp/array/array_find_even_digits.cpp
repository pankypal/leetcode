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

int numDigits(int num) {
    int count = 0;

    while (num > 0) {
        count++;

        num = num/10;
    }

    return count;
}

int main(int argc, const char * argv[]) {
    vector<int> vec {555,901,482,1771};
    int count = 0;

    for (int n : vec) {
        if (numDigits(n) % 2 == 0) {
            count++;
        }
    }

    cout << "Pankaj: " << count << endl;

    return 0;
}
