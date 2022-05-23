#         Original source code from:              #
###################################################
# https://github.com/chonyy/PageRank-HITS-SimRank #
###################################################

import numpy as np

class Graph:
    def __init__(self):
        self.nodes = []

    def contains(self, name):
        for node in self.nodes:
            if(node.name == name):
                return True
        return False

    # Return the node with the name, create and return new node if not found
    def find(self, name):
        if(not self.contains(name)):
            new_node = Node(name)
            self.nodes.append(new_node)
            return new_node
        else:
            return next(node for node in self.nodes if node.name == name)

    def add_edge(self, parent, child):
        parent_node = self.find(parent)
        child_node = self.find(child)

        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    def display(self):
        for node in self.nodes:
            print(f'{node.name} links to {[child.name for child in node.children]}')

    def sort_nodes(self):
        self.nodes.sort(key=lambda node: int(node.name))

    def display_hub_auth(self):
        for node in self.nodes:
            print(f'{node.name}  Auth: {node.old_auth}  Hub: {node.old_hub}')

    def normalize_auth_hub(self):
        auth_sum = sum(node.auth for node in self.nodes)
        hub_sum = sum(node.hub for node in self.nodes)

        for node in self.nodes:
            node.auth /= auth_sum
            node.hub /= hub_sum

    def normalize_pagerank(self):
        pagerank_sum = sum(node.pagerank for node in self.nodes)

        for node in self.nodes:
            node.pagerank /= pagerank_sum

    def get_auth_hub_list(self):
        auth_list = np.asarray([node.auth for node in self.nodes], dtype='float32')
        hub_list = np.asarray([node.hub for node in self.nodes], dtype='float32')

        return np.round(auth_list, 3), np.round(hub_list, 3)

    def get_pagerank_list(self):
        pagerank_list = np.asarray([node.pagerank for node in self.nodes], dtype='float32')
        return np.round(pagerank_list, 3)


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.auth = 1.0
        self.hub = 1.0
        self.pagerank = 1.0

    def link_child(self, new_child):
        for child in self.children:
            if(child.name == new_child.name):
                return None
        self.children.append(new_child)

    def link_parent(self, new_parent):
        for parent in self.parents:
            if(parent.name == new_parent.name):
                return None
        self.parents.append(new_parent)

    def update_auth(self):
        self.auth = sum(node.hub for node in self.parents)

    def update_hub(self):
        self.hub = sum(node.auth for node in self.children)

    def update_pagerank(self, d, n):
        in_neighbors = self.parents
        pagerank_sum = sum((node.pagerank / len(node.children)) for node in in_neighbors)
        random_jumping = d / n
        self.pagerank = random_jumping + (1-d) * pagerank_sum


def init_graph(fname):
    with open(fname) as f:
        lines = f.readlines()

    graph = Graph()

    for line in lines:
        [parent, child] = line.strip().split(',')
        graph.add_edge(parent, child)

    graph.sort_nodes()

    return graph

def PageRank_one_iter(graph, d):
    node_list = graph.nodes
    for node in node_list:
        node.update_pagerank(d, len(graph.nodes))
    graph.normalize_pagerank()
    # print(graph.get_pagerank_list())
    # print()


def PageRank(graph, d, iteration=100):
    for i in range(iteration):
        PageRank_one_iter(graph, d)


if __name__ == '__main__':

    iteration = 1000

    damping_factor = 0.15

    graph = init_graph('../data/hollins_id_out_id.csv')

    PageRank(graph, damping_factor, iteration)
    result = graph.get_pagerank_list()
    with open('../data/output.csv', 'w') as f:
        for i in range(len(result)):
            f.write(f'{i},{result[i]}\n')


