#include <iostream>
#include "vector"

using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> res;
    int row_start = 0;
    int row_end = matrix.size();
    int col_start = 0;
    int col_end = matrix[0].size();

    while (row_start < row_end && col_start < col_end) {
        // Top row
        for (int i = col_start; i < col_end; i++) {
            res.push_back(matrix[row_start][i]);
        }
        row_start++;

        // Right col
        for (int i = row_start; i < row_end; i++) {
            res.push_back(matrix[i][col_end-1]);
        }
        col_end--;

        if (row_start >= row_end || col_start >= col_end)
            break;

        // Bottom row
        for (int i = col_end-1; i >= col_start; i--) {
            res.push_back(matrix[row_end-1][i]);
        }
        row_end--;

        // Left Col
        for (int i = row_end-1; i >= row_start; i--) {
            res.push_back(matrix[i][col_start]);
        }
        col_start++;
    }

    return res;
}

int main(int argc, const char * argv[]) {
    vector<vector<int>> nums;
    nums.push_back({1});
    nums.push_back({2});
    nums.push_back({3});
    nums.push_back({4});
    nums.push_back({5});
    nums.push_back({6});
    nums.push_back({7});
    nums.push_back({8});
    nums.push_back({9});
    nums.push_back({10});
    vector<int> res = spiralOrder(nums);
    for (int n : res) {
        cout << n << ",";
    }
    cout << endl;
    return 0;
}
