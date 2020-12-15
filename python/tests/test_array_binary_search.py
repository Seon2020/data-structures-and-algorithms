from code_challenges.array_binary_search.array_binary_search import binary_search_recursive, get_high, binary_search_iterative

# Test recursive approach:
def test_recursive_one():
  actual = binary_search_recursive([1,2,3,4,5,6], 4)
  expected = 3
  assert actual == expected

def test_recursive_two():
  actual = binary_search_recursive([1,2,3,4,5,6,7], 666)
  expected = -1
  assert actual == expected

def test_recursive_three():
  actual = binary_search_recursive([111,222,333,444,555,666,777,888,999], 999)
  expected = 8
  assert actual == expected

# Test iterative approach:
def test_iterative_one():
  actual = binary_search_iterative([1,2,3,4,5,6], 4)
  expected = 3
  assert actual == expected

def test_iterative_two():
  actual = binary_search_iterative([1,2,3,4,5,6,7], 666)
  expected = -1
  assert actual == expected

def test_iterative_three():
  actual = binary_search_iterative([1,2,3,4,5,7,8,9,666], 666)
  expected = 8
  assert actual == expected
