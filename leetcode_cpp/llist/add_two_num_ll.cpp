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


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = nullptr;
        ListNode* prev = nullptr;
        int carry = 0;

        while (l1 || l2) {
            int sum = 0;

            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }

            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            sum += carry;

            ListNode* temp = new ListNode(sum%10);
            if (prev == nullptr) {
                res = temp;
            } else {
                prev->next = temp;
            }
            prev = temp;

            carry = sum/10;
        }

        if (carry > 0) {
            prev->next = new ListNode(carry);
        }

        return res;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;

    ListNode *node1 = new ListNode(3);
    ListNode *node2 = new ListNode(4, node1);
    ListNode *node3 = new ListNode(2, node2);
    ListNode *node7 = new ListNode(8, node3);

    ListNode *node4 = new ListNode(4);
    ListNode *node5 = new ListNode(6, node4);
    ListNode *node6 = new ListNode(5, node5);

    ListNode *res = sol.addTwoNumbers(node7, node6);

    while (res) {
        cout << res->val << ", ";
        res = res->next;
    }

    return 0;
}
