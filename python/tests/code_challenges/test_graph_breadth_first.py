import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph

def test_bfs(graph):
    nodes = graph.get_nodes()
    root = nodes[0]  # Assuming Pandora as the starting node
    actual = graph.breadth_first(root)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
    assert actual == expected or actual == ["Pandora", "Arendelle", "Monstropolis", "Metroville", "Naboo", "Narnia"]

def test_bfs_with_single_node(graph):
    single_node_graph = Graph()
    lone_node = single_node_graph.add_node("Lonely Island")
    assert single_node_graph.breadth_first(lone_node) == ["Lonely Island"]

def test_bfs_with_no_edges(graph):
    isolated_graph = Graph()
    isolated_graph.add_node("Isolated")
    isolated_graph.add_node("Still Isolated")
    nodes = isolated_graph.get_nodes()
    assert isolated_graph.breadth_first(nodes[0]) == ["Isolated"]

@pytest.mark.parametrize("node", ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"])
def test_bfs_from_each_node(graph, node):
    nodes = {n.value: n for n in graph.get_nodes()}
    start_node = nodes[node]
    result = graph.breadth_first(start_node)
    assert start_node.value in result

@pytest.fixture
def graph():
    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_edge(pandora, arendelle)
    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)
    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)
    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)
    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)
    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)

    return realms
