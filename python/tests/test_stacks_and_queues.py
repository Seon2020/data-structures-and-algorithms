import pytest 
from code_challenges.stacks_and_queues.stacks_and_queues import Node, InvalidOperationError, Stack, Queue

# Instantiate an empty stack
def test_new_empty_stack():
  stack = Stack()
  actual = stack.top
  expected = None
  assert actual == expected

def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected

def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected

def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected

def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected

def test_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert actual == expected

def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected

def test_peek_one():
  s = Stack()
  s.push("apple")
  s.push("banana")
  actual = s.peek()
  expected = "banana"
  assert actual == expected

def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"

def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"

def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected

def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("orange")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected

def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected

def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.peek()

    assert str(e.value) == "Method not allowed on empty collection"

def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected

def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected

def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"

def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected

def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected

def test_is_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.peek()

    assert str(e.value) == "Method not allowed on empty collection"

def test_exhausted():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("orange")
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
  