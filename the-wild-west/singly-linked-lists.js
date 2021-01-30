//  Class Node declaration.
class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

// Class SinglyLinkedList declaration.
class SinglyLinkedList {
    constructor(val) {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    //  Push method declaration. It takes a value and pushed it at the end of the list.
    push(val) {
        // Create a new node with the passed value.
        let node = new Node(val);
        // If there list doesn't have a head:
        if (!this.head) {
            // Make this node the head and the tail of the list.
            this.head = node;
            this.tail = this.head;
            // Increment the list's length.
            this.length++;
            // If the list had a head property already:
        } else {
            // Assigh the new node to be the next node of tha tail.
            this.tail.next = node;
            // Make the tail to be the new node and so the last added node becomes the tail of the list.
            this.tail = node;
            // Increment the length of the list.
            this.length++;
        }
        // Return the the list.
        return this;
    }
    // Pop method declaration. It will remove and return the last node of the list.
    pop() {
        // If the list doesn't have a head property return undefined.
        if (!this.head) return undefined;
        // Declare and initialised two wariables to keep track of the current node and the newtail.
        let current = this.head;
        let newTail = current;
        // While there is a next node in the list, keep iterating.
        while (current.next) {
            // For each iteration, the newTail becomes the current node and the current node becomes the next node.
            newTail = current;
            current = current.next;
        }
        // The tail is set to the newTail;
        this.tail = newTail;
        // The next value of tha tail is set to null;
        this.tail.next = null;
        // The length of the list is discremented.
        this.length--;
        // It the length of the list is 0, set the head and the tail to be null.
        if (this.length === 0) {
            this.head = null;
            this.tail = this.head;
        }
        // return the popped node.
        return current;
    }
}