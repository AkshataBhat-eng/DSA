var Solution = function(head) {
    this.head = head;
};

Solution.prototype.getRandom = function() {
    let result = this.head.val;
    let current = this.head.next;
    let index = 2;

    while (current !== null) {
        if (Math.floor(Math.random() * index) === 0) {
            result = current.val;
        }
        current = current.next;
        index++;
    }

    return result;
};