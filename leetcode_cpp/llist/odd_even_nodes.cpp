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

ListNode* oddEvenList(ListNode* head) {
    if (!head || !head->next)
        return head;

    ListNode *odd = head;
    ListNode *even = head->next;
    ListNode *evenStart = head->next;

    ListNode *curr = head;

    while (even && even->next) {
        odd->next = even->next;
        odd = odd->next;

        even->next = odd->next;
        even = even->next;
    }

    odd->next = evenStart;

    return head;
}

//1->2->3->4->5->null

int main(int argc, const char * argv[])
{
    ListNode* head = new ListNode(2);
    head->next = new ListNode(1);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(5);
    head->next->next->next->next = new ListNode(6);
    head->next->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next->next = new ListNode(7);

    oddEvenList(head);

    return 0;
}
