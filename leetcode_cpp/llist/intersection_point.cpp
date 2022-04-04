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

ListNode* getIntersectionNode(ListNode *headA, ListNode *headB)
{
    if (!headA || !headB) {
        return nullptr;
    }

    ListNode* list1 = headA;
    ListNode* list2 = headB;

    while (list1 && list2) {
        list1 = list1->next;
        list2 = list2->next;
    }

    ListNode* bigger = nullptr;
    ListNode* smaller = nullptr;

    if (!list1 && !list2) {
        bigger = headB;
        smaller = headA;
    } else if (list2) {
        bigger = headB;
        smaller = headA;
    } else if (list1) {
        bigger = headA;
        smaller = headB;
    }

    if (bigger == headA) {
        ListNode* temp1 = headA;
        while (list1) {
            list1 = list1->next;
            temp1 = temp1->next;
        }

        while (temp1 != smaller) {
            temp1 = temp1->next;
            smaller = smaller->next;
        }
    } else {
        ListNode* temp1 = headB;
        while (list2) {
            list2 = list2->next;
            temp1 = temp1->next;
        }

        while (temp1 != smaller) {
            temp1 = temp1->next;
            smaller = smaller->next;
        }
    }


    return smaller;
}

ListNode* getIntersectionNode1(ListNode *headA, ListNode *headB)
{
    if (!headA || !headB) {
        return nullptr;
    }

    ListNode* list1 = headA;
    ListNode* list2 = headB;

    while (list1 != list2) {
        list1 = list1->next;
        list2 = list2->next;

        if (list1 == list2) {
            return list1;
        }

        if (list1 == nullptr) {
            list1 = headB;
        }

        if (list2 == nullptr) {
            list2 = headA;
        }
    }

    return list1;
}

int main(int argc, const char * argv[])
{
    ListNode* head1 = new ListNode(2);
    head1->next = new ListNode(2);

    ListNode* head2 = new ListNode(2);
    head2->next = new ListNode(2);



    ListNode* joint = head1->next->next = head2->next->next = new ListNode(4);
    joint->next = new ListNode(5);
    joint->next->next = new ListNode(4);

    cout << "intersection in lists: " << getIntersectionNode1(head1, head2) << endl;

    return 0;
}
