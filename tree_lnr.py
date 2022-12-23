class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.childs = []


class Tree(object):
    def __init__(self):
        self.root = None
        self.result = []
        self.way = []
        self.cur_address = 0

    def read_tree(self, f):
        # f = open('tree.txt', 'r')
        self.root = TreeNode(int(f.readline()))
        prev_nodes = [self.root]
        data = f.readlines()
        for s in data:
            cur_nodes = []
            nodes = s.split(',')
            for i in range(len(prev_nodes)):
                if nodes[i] != ' ':
                    for k in nodes[i].split():
                        prev_nodes[i].childs.append(TreeNode(int(k)))
                    cur_nodes += prev_nodes[i].childs
            prev_nodes = [i for i in cur_nodes]

    def print_tree(self):
        self.print_node(self.root)

    def print_node(self, node: TreeNode):
        print(node.value)
        for i in node.childs:
            self.print_node(i)

    def in_order_print(self, node: TreeNode):
        if not node.childs:
            print(node.value)
            return
        self.in_order_print(node.childs[0])
        print(node.value)
        for i in range(1, len(node.childs)):
            self.in_order_print(node.childs[i])

    def in_order(self, node: TreeNode, value: int):
        if not node.childs:
            self.way.append(node.value)
            if node.value == value:
                self.result.append(self.cur_address)
            self.cur_address += 1
            return
        self.in_order(node.childs[0], value)
        self.way.append(node.value)
        if node.value == value:
            self.result.append(self.cur_address)
        self.cur_address += 1
        for i in range(1, len(node.childs)):
            self.in_order(node.childs[i], value)

    def in_order_search(self, value: int) -> dict:
        self.result = []
        self.way = []
        self.cur_address = 0
        self.in_order(self.root, value)
        return {'way': self.way, 'value': value, 'result': self.result}


if __name__ == '__main__':
    f = open('tree.txt', 'r')
    tree = Tree()
    tree.read_tree(f)
    tree.print_tree()
    print('----')
    tree.in_order_print(tree.root)
    print('----')
    ans = tree.in_order_search(2)
    print(ans['way'])
    print(ans['value'])
    print(ans['result'])
