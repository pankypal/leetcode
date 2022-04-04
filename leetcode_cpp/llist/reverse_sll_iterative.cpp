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

ListNode* reverseList(ListNode* head) {
    ListNode *curr = head;
    ListNode *prev = nullptr;
    ListNode *next = head;

    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}


int main(int argc, const char * argv[])
{
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    reverseList(head);

    return 0;
}
