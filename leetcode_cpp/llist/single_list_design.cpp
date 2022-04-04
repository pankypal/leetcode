//
//  main.cpp
//  leetcode
//
//  Created by pankaj pal on 08/02/21.
//  Copyright © 2021 pankaj pal. All rights reserved.
//

#include <iostream>


using namespace std;

struct Node {
    int data;
    struct Node* next;

    Node(int val) : data(val), next(nullptr) {};
};

class MyLinkedList {
private:
    struct Node* head;
    int len = 0;

public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        head = nullptr;
    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (head == nullptr)
            return -1;

        Node* curr = head;
        while(index--)
        {
            if(curr->next==nullptr) return -1;
            curr = curr->next;
        }
        return curr->data;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        Node* node = new Node(val);

        node->next = head;
        head = node;
        len++;
    }

    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        if (len == 0) {
            addAtHead(val);
            return;
        }
        Node* curr = head;
        Node* node = new Node(val);

        while(curr->next != nullptr) {
            curr = curr->next;
        }

        curr->next = node;
        len++;
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {

        if (index == 0){
            addAtHead(val);
            return;
        }
        index--;

        Node* node = new Node(val);
        Node* curr = head;

        while (index) {
            if (curr->next == nullptr)
                return;

            curr = curr->next;
            index--;
        }

        node->next = curr->next;
        curr->next = node;
        len++;
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (!head)
            return;

        if (index > len-1) return;

        if (index == 0) {
            head = head->next;
            return;
        }

        Node* curr = head;
        index--;

        while(index) {
            if (curr->next == nullptr) {
                return;
            }

            curr = curr->next;
            index--;
        }

        curr->next = curr->next->next;
        len--;
    }
};

int main(int argc, const char * argv[])
{

    MyLinkedList* obj = new MyLinkedList();

    obj->addAtIndex(0, 10);
    obj->addAtIndex(0, 20);
    obj->addAtIndex(1, 30);

    cout << obj->get(0) << endl;

    return 0;
}
