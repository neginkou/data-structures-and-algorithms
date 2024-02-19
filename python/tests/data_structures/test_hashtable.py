import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

# @pytest.mark.skip("TODO")
def test_set_apple():
    hashtable = Hashtable()
    actual = hashtable.set("apple", "Used for apple sauce")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_no_key():
    hashtable = Hashtable()
    actual = hashtable.has("John Wayne")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_all_keys():
    hashtable = Hashtable()
    hashtable.set("Butter", "Good for cooking")
    hashtable.set("Water", "Stay hydrated")
    hashtable.set("Beer", "So good")
    actual = hashtable.keys()
    expected = ["Butter", "Water", "Beer"]
    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_collision():
    hashtable = Hashtable()
    hashtable.set("Apple", "Good for apple sauce")
    actual = hashtable.set("Apple", "Good for the soul")
    expected = "Good for the soul"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_hash():
    hashtable = Hashtable()
    actual = hashtable._hash("Negin")
    assert 0 <= actual < hashtable.size

# def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("arash", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["arash", 30]]]

    assert actual == expected
