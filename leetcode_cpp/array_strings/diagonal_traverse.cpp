#include <iostream>
#include "vector"

using namespace std;

vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
    vector<int> res;
    int rsize = (int)matrix.size();

    if (rsize == 0)
        return res;

    int csize = (int)matrix[0].size();

    vector<vector<int>> diags(rsize+csize-1);
    for (int i = 0; i < rsize; i++) {
        for (int j = 0; j < csize; j++) {
            diags[i+j].push_back(matrix[i][j]);
        }
    }

    for (int i = 0; i < rsize+csize-1; i++) {
        if (i%2==0) {
            reverse(diags[i].begin(), diags[i].end());
        }
    }

    for (auto r : diags) {
        for (auto c : r) {
            res.push_back(c);
        }
    }

    return res;
}

int main(int argc, const char * argv[]) {
    vector<vector<int>> nums;
    nums.push_back({1,2,3});
    nums.push_back({4,5,6});
    nums.push_back({7,8,9});
    vector<int> res = findDiagonalOrder(nums);
    for (int n : res) {
        cout << n << ",";
    }
    cout << endl;
    return 0;
}
