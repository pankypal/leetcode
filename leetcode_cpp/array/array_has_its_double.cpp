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

int main(int argc, const char * argv[]) {
    vector<int> arr {3,1,7,11};
    set<int> mapValues;
    bool found = false;

    for (int n : arr) {
        if (mapValues.find(n*2) != mapValues.end()
            || ((n%2 == 0) && (mapValues.find(n/2) != mapValues.end()))) {
            found = true;
            break;
        }

        mapValues.insert(n);
    }

    cout << "Found: " << found << endl;



    return 0;
}
