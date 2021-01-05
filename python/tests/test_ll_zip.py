from code_challenges.linked_list.linked_list import LinkedList, Node
from code_challenges.ll_zip.ll_zip import zipLists

def test_same_size_lists():
  list1 = LinkedList()
  list1.append(1)
  list1.append(2)
  list1.append(3)
  list2 = LinkedList()
  list2.append(4)
  list2.append(5)
  list2.append(6)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{4}->{2}->{5}->{3}->{6}->NULL"
  assert actual == expected

def test_list1_shorter():
  list1 = LinkedList()
  list1.append(1)
  list1.append(2)
  list2 = LinkedList()
  list2.append(4)
  list2.append(5)
  list2.append(6)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{4}->{2}->{5}->{6}->NULL"
  assert actual == expected

def test_list1_shorter_plus():
  list1 = LinkedList()
  list1.append(1)
  list1.append(2)
  list2 = LinkedList()
  list2.append(4)
  list2.append(5)
  list2.append(6)
  list2.append(7)
  list2.append(8)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{4}->{2}->{5}->{6}->{7}->{8}->NULL"
  assert actual == expected

def test_list1_longer():  
  list1 = LinkedList()
  list1.append(1)
  list1.append(2)
  list1.append(3)
  list2 = LinkedList()
  list2.append(4)
  list2.append(5)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{4}->{2}->{5}->{3}->NULL"
  assert actual == expected

def test_list1_longer_plus():  
  list1 = LinkedList()
  list1.append(1)
  list1.append(2)
  list1.append(3)
  list1.append(7)
  list1.append(8)
  list2 = LinkedList()
  list2.append(4)
  list2.append(5)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{4}->{2}->{5}->{3}->{7}->{8}->NULL"
  assert actual == expected
