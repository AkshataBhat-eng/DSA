var mergeKLists = function(lists) {
    if (!lists.length) return null;

    while (lists.length > 1) {
        let a = lists.shift();
        let b = lists.shift();
        const merged = mergeTwoLists(a, b);
        lists.push(merged);
    }
    return lists[0]

};
function mergeTwoLists(l1, l2) {
  let dummy = new ListNode(0), current = dummy;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      current.next = l1;
      l1 = l1.next;
    } else {
      current.next = l2;
      l2 = l2.next;
    }
    current = current.next;
  }
  current.next = l1 || l2;
  return dummy.next;
}