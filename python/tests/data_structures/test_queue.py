import pytest
from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError

def test_exists():
    assert Queue

def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.peek()
    expected = "apple"
    assert actual == expected

def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
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
    actual = q.is_empty()
    expected = True
    assert actual == expected

def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
