import pytest
from code_challenges.get_edge.get_edge import get_edge
from code_challenges.graphs.graphs import Graph

def test_metroville_to_pandora(flights):
    graph = flights[0]
    routes = [flights[4], flights[1]]
    actual = get_edge(graph, routes)
    assert actual == (True, 82)

def test_arendelle_to_monstropolis_to_neboo(flights):
    graph = flights[0]
    routes = [flights[3], flights[5], flights[6]]
    actual = get_edge(graph, routes)
    assert actual == (True, 115)

def test_naboo_to_pandora(flights):
    graph = flights[0]
    route = [flights[6], flights[1]]
    actual = get_edge(graph, route)
    assert actual == (False, 0)

def test_narnia_to_arendelle_to_neboo(flights):
    graph = flights[0]
    route = [flights[2], flights[3], flights[6]]
    actual = get_edge(graph, route)
    assert actual == (False, 0)

def test_graph_empty():
    graph = Graph()
    routes = []
    actual = get_edge(graph, routes)
    assert actual == (False, 0)

@pytest.fixture
def flights():
    graph = Graph()
    pandora = graph.add_node("pandora")
    arendelle = graph.add_node("arendelle")
    metroville = graph.add_node("metroville")
    monstropolis = graph.add_node("monstropolis")
    narnia = graph.add_node("narnia")
    naboo = graph.add_node("naboo")
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(monstropolis, naboo, 73)
    graph.add_edge(narnia, naboo, 250)
    return [graph, pandora, narnia, arendelle, metroville, monstropolis, naboo]



 