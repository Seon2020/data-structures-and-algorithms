from code_challenges.depth_first.depth_first import Graph

def test_depth_first_single():
    graph = Graph()
    a = graph.add_node('a')
    actual = graph.depth_first(a)
    assert actual == [a]

def test_depth_first_multiple():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    actual = graph.depth_first(a)
    assert actual == [a, b, d, c]

def test_depth_first_many():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(b, f)
    graph.add_edge(f, g)
    actual = graph.depth_first(a)
    assert actual == [a, b, f, g, c, d, e]