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

int main(int argc, const char * argv[]) {
    vector<int> vec {0, 2};

    vector<int> neg;
    vector<int> pos;

    for (int i : vec) {
        if (i < 0)
            neg.insert(neg.begin(), i*i);
        else
            pos.push_back(i*i);
    }

    vector<int> res;
    int i = 0;
    int j = 0;

    for (; i < neg.size() && j < pos.size();) {
        if (neg[i] < pos[j]) {
            res.push_back(neg[i]);
            i++;
        } else {
            res.push_back(pos[j]);
            j++;
        }
    }

    while (i < neg.size()) {
        res.push_back(neg[i]);
        i++;
    }

    while (j < pos.size()) {
        res.push_back(pos[j]);
        j++;
    }

    for (int v : res)
        cout << v << ",";

    cout <<endl;


    //cout << "Pankaj: " << count << endl;

    return 0;
}
