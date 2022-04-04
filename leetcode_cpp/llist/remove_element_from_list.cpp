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

ListNode* removeElements(ListNode* head, int val) {
    if (!head)
        return nullptr;
    
    ListNode *curr = head;
    while (curr && curr->val == val) {
        curr = curr->next;
    }
    head = curr;

    while (curr && curr->next) {
        if (curr->next->val == val)
            curr->next = curr->next->next;
        else
            curr = curr->next;
    }

    return head;
}


int main(int argc, const char * argv[])
{
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(2);
    head->next->next->next = new ListNode(1);

    removeElements(head, 2);

    return 0;
}
