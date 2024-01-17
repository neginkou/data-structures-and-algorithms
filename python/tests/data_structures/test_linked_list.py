import pytest
from data_structures.linked_list import LinkedList, TargetError


def test_exists():
    assert LinkedList


@pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


@pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


@pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


@pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


@pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def test_append_empty():
    linked_list = LinkedList()
    linked_list.append("apple")
    assert str(linked_list) == "{ apple } -> NULL"

def test_append_non_empty():
    linked_list = LinkedList()
    linked_list.insert("banana")
    linked_list.append("apple")
    assert str(linked_list) == "{ banana } -> { apple } -> NULL"

def test_insert_before_single():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert_before("apple", "banana")
    assert str(linked_list) == "{ banana } -> { apple } -> NULL"

def test_insert_before_multi():
    linked_list = LinkedList()
    linked_list.insert("carrot")
    linked_list.insert("banana")
    linked_list.insert_before("banana", "apple")
    assert str(linked_list) == "{ apple } -> { banana } -> { carrot } -> NULL"

def test_insert_before_nonexistent():
    linked_list = LinkedList()
    linked_list.insert("banana")
    with pytest.raises(TargetError):
        linked_list.insert_before("apple", "carrot")

def test_insert_after_single():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert_after("apple", "banana")
    assert str(linked_list) == "{ apple } -> { banana } -> NULL"

def test_insert_after_multi():
    linked_list = LinkedList()
    linked_list.insert("carrot")
    linked_list.insert("banana")
    linked_list.insert_after("banana", "apple")
    assert str(linked_list) == "{ banana } -> { apple } -> { carrot } -> NULL"

def test_insert_after_nonexistent():
    linked_list = LinkedList()
    linked_list.insert("banana")
    with pytest.raises(TargetError):
        linked_list.insert_after("apple", "carrot")


