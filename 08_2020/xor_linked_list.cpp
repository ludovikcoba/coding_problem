/*
An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that 
converts between nodes and memory addresses.
*/
#include <iostream>
#include <stdint.h>

#define MASK 0x00000000

class Node{
    public:

        int element;
        Node * both = NULL;

};

Node* XOR(Node* prev, Node* next) {
    return (Node *)((uintptr_t)(prev) ^ (uintptr_t)(next));
}

class XORLinkedList{
    Node * head = NULL;
    Node * tail = NULL;
    int count = 0;

    public:

        XORLinkedList(){};

        void add(int element){

            Node *n = new Node;
            n->element = element;

            if(head == NULL){
                head = tail = n;
                
            }else if (tail->both == NULL){

                tail->both = n;
                n->both = n;
                tail = n;

            }else{
                
                n->both = tail;
                tail->both = XOR(tail->both, n);
            }

            count++;
        };

        Node *get(int i){

            if(head == NULL || i >= count) return NULL;       

            Node * current = head;
            Node * next = head->both;

            while (i>0)
            {
                Node * temp = next;
                next = XOR(next, current);
                current = temp;
                i--; 
            }
            return current;
        };

};