# Assignment5
## Assignment 5
# Circular and Double Linked List in C Programming



This repository contains C programming examples and explanations for implementing Circular and Double Linked Lists. Linked lists are fundamental data structures that provide dynamic memory allocation and efficient insertion and deletion of elements. In this project, we explore both circular and double linked list implementations with code examples and explanations.



## Introduction to Linked Lists

Linked lists are data structures that consist of nodes, each containing data and a reference (or link) to the next node. In a double linked list, each node also has a link to the previous node. Circular linked lists are a variant where the last node's link points back to the first node.

## Circular Linked List

### Features of Circular Linked List

- Elements form a loop, where the last element points back to the first element.
- Dynamic size: Elements can be easily inserted and removed.
- Memory-efficient: Space is allocated as needed, unlike arrays with fixed sizes.

### Implementation of Circular Linked List

The circular linked list implementation includes the following functions:

- `createNode`: Creates a new node.
- `insertAtBeginning`: Inserts a new node at the beginning.
- `insertAtEnd`: Inserts a new node at the end.
- `deleteFromBeginning`: Deletes a node from the beginning.
- `deleteFromEnd`: Deletes a node from the end.
- `display`: Displays the elements of the circular linked list.


   

## Double Linked List

### Features of Double Linked List

- Bidirectional traversal: Nodes can be traversed in both forward and backward directions.
- Efficient deletion: Removing a node only requires updating two links.
- Supports more operations: Insertions and deletions are more flexible.

### Implementation of Double Linked List

The double linked list implementation includes the following functions:

- `createNode`: Creates a new node.
- `insertAtBeginning`: Inserts a new node at the beginning.
- `insertAtEnd`: Inserts a new node at the end.
- `deleteFromBeginning`: Deletes a node from the beginning.
- `deleteFromEnd`: Deletes a node from the end.
- `displayForward`: Displays the elements in forward order.
- `displayBackward`: Displays the elements in backward order.






Contributions are welcome! If you find any issues or want to add more features/examples, feel free to open a pull request.



