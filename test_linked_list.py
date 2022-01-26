from linked_list import *


def test_len():
    ll = LinkedList()
    assert len(ll) == 0

def test_add_node():
    ll = LinkedList()    
    assert str(ll.add_node(12)) == '12'

def test_add_node_as_head():
    ll = LinkedList()
    ll.add_node(12)
    ll.add_node_as_head('abc')
    assert str(ll) == 'abc->12'

def test_add_multiple_nodes():
    ll = LinkedList()
    ll.add_multiple_nodes(["banana","mango","grapes","orange"])
    assert str(ll) == 'banana->mango->grapes->orange'

def test_insert_at():
    ll = LinkedList()
    ll.add_multiple_nodes(["banana","mango","grapes","orange"])
    ll.insert_at(2,"blueberry")
    assert str(ll) == 'banana->mango->blueberry->grapes->orange'

def test_remove_at():
    ll = LinkedList()
    ll.add_multiple_nodes(["banana","mango","grapes","orange"])
    ll.remove_at(2)
    assert str(ll) == 'banana->grapes->orange'