def reverse_list(ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    prev = None
    current = ll.head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    ll.head = prev
    return ll



