from code_challenges.graphs.graphs import Graph

def get_edge(graph, routes):
    if graph.get_nodes() != None and routes:

        weight_total = 0

        for i, dest in enumerate(routes):
            connecting_flights = graph.get_neighbors(dest)
            if i < len(routes) - 1: next_dest = routes[i + 1]
            else: break

            connection_list = [x.vertex for x in connecting_flights]

            if next_dest not in connection_list:
                return (False, 0)

            weight_next_dest = [x.weight for x in connecting_flights if x.vertex == next_dest]
            
            weight_total += sum(weight_next_dest)

        return (True, weight_total)
    return (False, 0)