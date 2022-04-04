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
    struct Node* prev;

    Node(int val) : data(val), next(nullptr), prev(nullptr) {};
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
        if (index+1 > len)
            return -1;

        Node* curr = head;
        for (int i = 0; i < index; i++)
            curr = curr->next;

        return curr->data;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        Node* node = new Node(val);

        node->next = head;

        if (head) {
            head->prev = node;
        }
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
        node->prev = curr;
        len++;
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {

        if (index > len || index < 0)
            return;

        if (index == 0){
            addAtHead(val);
            return;
        }

        if (index == len) {
            addAtTail(val);
            return;
        }

        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }

        Node *node = new Node(val);
        node->next = curr;
        node->prev = curr->prev;

        node->prev->next = node;
        node->next->prev = node;

        len++;
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {

        if (index >= len) return;

        if (index == 0) {
            head = head->next;
            return;
        }

        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }

        curr->prev->next = curr->next;
        if (curr->next) {
            curr->next->prev = curr->prev;
        }

        len--;
    }
};

int main(int argc, const char * argv[])
{

    MyLinkedList* obj = new MyLinkedList();

    obj->addAtHead(7);
    obj->addAtHead(2);
    obj->addAtHead(1);
    obj->addAtIndex(3, 0);
    obj->deleteAtIndex(2);
    obj->addAtHead(6);
    obj->addAtTail(4);
    cout << obj->get(4) << endl;
    obj->addAtHead(4);
    obj->addAtIndex(5, 0);
    obj->addAtHead(6);

    return 0;

    // 1 2 7 0
}
