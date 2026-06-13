N = int(input())
tree = []

class Node():
    def __init__(self, name, id, children):
        self.name = name
        self.id = id
        self.children = children

    def find_node(self, id):
        if self.id == id:
            return self
        for child in self.children:
            res = child.find_node(id)
            if res is not None:
                return res
        return None


for _ in range(N):
    node_id, name, parent = input().split()
    node_id, parent = int(node_id), int(parent)

    if parent == 0:
        tree.append(Node(name, node_id, []))
    else:
        for root in tree:
            parent_node = root.find_node(parent)
            if parent_node:
                parent_node.children.append(Node(name, node_id, []))
                break


for root in tree:
    print(root.name)

    for child1 in root.children:
        print("  " + child1.name)

        for child2 in child1.children:
            print("    " + child2.name)