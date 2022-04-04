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

bool isPalindrome(ListNode* head) {
    ListNode *slow = head;
    ListNode *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    slow = reverseList(slow);
    fast = head;

    while (slow && fast) {
        if (slow->val != fast->val)
            return false;

        slow = slow->next;
        fast = fast->next;
    }

    return true;
}

//2->1->1->2->null

int main(int argc, const char * argv[])
{
    ListNode* head = new ListNode(2);
    head->next = new ListNode(1);
    head->next->next = new ListNode(2);

    isPalindrome(head);

    return 0;
}
