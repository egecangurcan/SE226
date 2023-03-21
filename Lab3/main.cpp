#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Queue {
public:
    Node* back;
    Node* front;
    int counter;

public:
    Queue() {
        front = NULL;
        back = NULL;
        counter = 0;
    }

bool isEmpty() {
    return (counter == 0);
}

int size(){
    return counter;
}


void enqueue(int data) {
    Node *newNode = new Node();
    newNode->data = data;
    newNode->next = NULL;
    if (isEmpty()) {
        front = back = newNode;
    } else {
        back->next = newNode;
        back = newNode;
    }
    counter++;
}

void dequeue() {

    if (isEmpty()) {
        cout << "Underflow condition." << endl;
        return;
    }

    Node* temp = front;
    front = front->next;

    delete temp;
    counter--;
}

int top() {
    if (isEmpty()) {
        cout << "Queue is empty." << endl;
        return -1;
    }
    return front->data;
    }
};

int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(25);
    q.enqueue(30);

    cout << "Queue size: " << q.size() << endl;
    cout << "Top element of the Queue: " << q.top() << endl;

    q.dequeue();

    cout << "Queue size: " << q.size() << endl;
    cout << "Top element of the Queue: " << q.top() << endl;

    q.dequeue();

    cout << "Queue size: " << q.size() << endl;
    cout << "Top element of the Queue: " << q.top() << endl;

    q.dequeue();

    cout << "Queue size: " << q.size() << endl;
    cout << "Top element of the Queue: " << q.top() << endl;

    q.enqueue(5);

    cout << "Queue size: " << q.size() << endl;
    cout << "Top element of the Queue: " << q.top() << endl;

    
}
