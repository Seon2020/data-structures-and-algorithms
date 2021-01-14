import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_pseudoqueue_enqueue_one():
  q = PseudoQueue()
  q.enqueue("orange")
  actual = q.input.peek()
  expected = "orange"
  assert actual == expected

def test_pseudoqueue_enqueue_several():
  q = PseudoQueue()
  q.enqueue("orange")
  q.enqueue("apple")
  actual = q.input.peek()
  expected = "apple"
  assert actual == expected

def test_pseudoqueue_dequeue_one():
  q = PseudoQueue()
  q.enqueue("orange")
  actual = q.dequeue()
  expected = "orange"
  assert actual == expected

def test_pseudoqueue_dequeue_several():
  q = PseudoQueue()
  q.enqueue("orange")
  q.enqueue("apple")
  q.enqueue("lime")
  q.dequeue()
  q.dequeue()
  actual = q.dequeue()
  expected = "orange"
  assert actual == expected
