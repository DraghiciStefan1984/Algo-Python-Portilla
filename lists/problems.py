def cycle_check(node):
    marker1=marker2=node
    while marker1!=None and marker2.next_node!=None:
        marker1=marker1.next_node
        marker2=marker2.next_node.next_node
        if marker2==marker1:
            return True
    return False