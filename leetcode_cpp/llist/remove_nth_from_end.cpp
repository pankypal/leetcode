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

ListNode* removeNthFromEnd(ListNode* head, int n)
{
    if (head == nullptr) {
        return nullptr;
    }

    ListNode* ptr = head;

    while (n--) {
        ptr = ptr->next;
    }

    ListNode *curr = head;
    ListNode *prev = nullptr;
    while (ptr) {
        ptr = ptr->next;
        prev = curr;
        curr = curr->next;
    }

    if (prev == nullptr) {
        head = head->next;
    } else {
        prev->next = curr->next;
    }

    delete curr;

    return head;
}


int main(int argc, const char * argv[])
{
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    removeNthFromEnd(head, 2);
    return 0;
}
