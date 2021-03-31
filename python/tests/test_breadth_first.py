from code_challenges.breadth_first.breadth_first import Graph

def test_breadth_first_single():
    graph = Graph()
    a = graph.add_node('a')
    actual = graph.breadth_first(a)
    assert actual == [a]

def test_breadth_first_multiple():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    actual = graph.breadth_first(a)
    assert actual == [a, b, c]

def test_breadth_first_many():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(b, f)
    actual = graph.breadth_first(a)
    assert actual == [a, b, c, f, d, e]

