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
    vector<int> vec {8,4,5,0,0,0,0,7};

    int countZ = (int)std::count(vec.begin(), vec.end(), 0);
    int sz = (int)vec.size();
    int destination = sz + countZ -1;

    for (int i = sz-1; i >= 0 ; i--) {
        if (vec[i] == 0) {
            for (int r = 1; r <= 2; r++) {
                if (destination > sz-1) {
                    destination--;
                } else {
                    vec[destination] = 0;
                    destination--;
                }
            }
        } else {
            if (destination > sz-1) {
                destination--;
                continue;
            }

            vec[destination--] = vec[i];
        }
    }

    for (int v : vec)
        cout << v << ",";

    cout <<endl;

    return 0;
}
