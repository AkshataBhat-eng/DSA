var removeNthFromEnd = function(head, n) {

    let temp = new ListNode(0);
    temp.next = head;
    let listLength = 0;
    let first = head;
    
    while(first) {
        listLength++;
        first = first.next;
    }

    listLength -= n;
    first = temp;
    while(listLength > 0) {
        listLength--;
        first = first.next;
    }
    first.next = first.next.next;
    return temp.next;
};