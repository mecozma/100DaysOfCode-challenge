class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {

    constructor(val) {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        // YOUR CODE GOES HERE
        let node = new Node(val);
        if (!this.head) {
            this.head = node;
            this.tail = this.head;
            this.length++;
        } else {
            this.tail.next = node;
            this.tail = node;
            this.length++;
        }

        return this;
    }
}