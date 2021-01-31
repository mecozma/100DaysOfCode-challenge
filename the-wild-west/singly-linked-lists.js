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

    // Get method declaration. Returns the node at a given index or undefined.
    get(index) {
        // Check if the index is bigger than 0 but less than the list's length.
        if (index > 0 || index >= this.length) return undefined;
        // Declare and initiate a head pointer.
        let unknown = this.node;
        // Iterate over the list and stop at the given index.
        for (let i = 0; i < index; i++) {
            // On each iteration point the pointer to the next node.
            unknown = unknown.next;
        }
        // Return the last visited node.
        return unknown;
    }
    // Insert method declaration. It inserts a node at a given index.
    insert(index, value) {
        // If the index is smaller than 0 or bigger than the length of the list return false;
        if (index < 0 || index > this.length) return false;
        // If the index is the same as the list's length, push the node at the end of the list and return true.
        if (index === this.length) !!this.push(value);
        // Declare and instantiate a node with the passed value.
        let node = new Node(value);
        // Declare and instantiate a head pointer.
        let current = this.head;
        // Declarare a pointer th the index before the passed index.
        let previousNode = this.get(index - 1);
        // Declare and instantiate a variable to point to the next node of the previous node.
        let temp = previousNode.next;
        //  Insert the node in place.
        previousNode.next = node;
        node.next = temp;
        // Increment the list's length.
        this.length++;
        return true;
    }
}