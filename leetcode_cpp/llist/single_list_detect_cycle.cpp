//
//  main.cpp
//  leetcode
//
//  Created by pankaj pal on 08/02/21.
//  Copyright © 2021 pankaj pal. All rights reserved.
//

#include <iostream>


using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode *detectCycle(ListNode *head) {
    if (head == nullptr)
        return nullptr;

    ListNode* slow = head;
    ListNode* fast = head;
    ListNode* node = nullptr;

    bool foundCycle = false;

    while(fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            foundCycle = true;
            break;
        }
    }

    if (foundCycle) {
        ListNode* curr = head;
        node = head;

        while (curr != slow) {
            curr = curr->next;
            slow = slow->next;
        }
    }

    return foundCycle ? slow : nullptr;
}

// 1 2 3 4 5 6  7
// 1 3 5 7 9 11 13

int main(int argc, const char * argv[])
{
    ListNode* head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head->next;

    cout << "Detect Cycle: " << detectCycle(head)->val << endl;

    return 0;
}
