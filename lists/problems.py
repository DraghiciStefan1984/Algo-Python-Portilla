def cycle_check(node):
    marker1=marker2=node
    while marker1!=None and marker2.next_node!=None:
        marker1=marker1.next_node
        marker2=marker2.next_node.next_node
        if marker2==marker1:
            return True
    return False


def link_reversal(head):
    current=head
    previous_node=next_node=None

    while current:
        next_node=current.next_node
        current.next_node=previous_node
        previous_node=current
        current=next_node
    return previous_node


def nth_to_the_last(n, head):
    left_pointer=right_pointer=head
    for i in range(n-1):
        if not right_pointer.next_node:
            raise LookupError('n is larger than the linked list')
        right_pointer=right_pointer.next_node
    while right_pointer.next_node:
        left_pointer=left_pointer.next_node
        right_pointer=right_pointer.next_node
    return left_pointer