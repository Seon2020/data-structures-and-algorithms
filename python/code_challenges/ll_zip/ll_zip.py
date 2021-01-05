def zipLists(list1, list2):
  list1_current = list1.head
  list2_current = list2.head

  while list1_current and list2_current:
    list1_next = list1_current.next
    list2_next = list2_current.next

    list1_current.next = list2_current
    list2_current.next = list1_next

    last_list1_current = list1_current.next

    list1_current = list1_next
    list2_current = list2_next
    
  if not list1_current and list2_current:
    last_list1_current.next = list2_current

  return list1


 