from Unit_1.Lecture_3.graphs import *

nodes = list()
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


edges = list()
edges.append(Edge(g.getNode('ABC'), g.getNode('BAC')))
edges.append(Edge(g.getNode('ABC'), g.getNode('ACB')))
edges.append(Edge(g.getNode('ACB'), g.getNode('CAB')))
edges.append(Edge(g.getNode('BAC'), g.getNode('BCA')))
edges.append(Edge(g.getNode('BCA'), g.getNode('CBA')))
edges.append(Edge(g.getNode('CBA'), g.getNode('CAB')))

for n in edges:
    g.addEdge(n)


def DFS(graph, start, end, path, shortest):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest)
                if new_path is not None:
                    shortest = new_path
        else:
            print('Already visited')
    return shortest


DFS(g, g.getNode("ABC"), g.getNode("CBA"), [], None)
