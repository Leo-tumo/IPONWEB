from BST import whiskey

BLACK = 0
RED = 1
NIL = None


class Node:
    def __init__(self, item):
        self.item = item
        self.parent = NIL
        self.left = NIL
        self.right = NIL
        self.color = RED


class RBTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = BLACK
        self.nil.left = NIL
        self.nil.right = NIL
        self.root = self.nil

    def search_tree_helper(self, node, key):
        if node == self.nil or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def delete_fix(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == BLACK and s.right.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.right.color == BLACK:
                        s.left.color = BLACK
                        s.color = RED
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == BLACK and s.left.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.left.color == BLACK:
                        s.right.color = BLACK
                        s.color = RED
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def __rb_transplant(self, u, v):
        if u.parent is NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, key):
        z = self.nil
        while node != self.nil:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.nil:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.delete_fix(x)

    def fix_insert(self, k):
        while k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK

    def _search(self, k):
        return self.search_tree_helper(self.root, k)

    def search(self, k):
        x = self.root
        try:
            while x != NIL and k != x.item:
                if k < x.item:
                    x = x.left
                else:
                    x = x.right
            return x
        except TypeError:
            return NIL

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.nil:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)

        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left != self.nil:
            return self.maximum(x.left)

        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = NIL
        node.item = key
        node.left = self.nil
        node.right = self.nil
        node.color = RED

        y = NIL
        x = self.root

        while x != self.nil:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is NIL:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent is NIL:
            node.color = BLACK
            return

        if node.parent.parent is NIL:
            return

        self.fix_insert(node)

    def delete(self, item):
        self.delete_node_helper(self.root, item)

    def __repr__(self):
        lines = []
        self.print_tree(self.root, lines)
        return '\n'.join(lines)

    def print_tree(self, node, lines, level=0):
        if node.item != 0:
            self.print_tree(node.left, lines, level + 1)
            lines.append(('\033[1;31m' if node.color else '\033[1;30m') + '-' * 10 * level + '> ' +
                         str(node.item) + ' ')
            self.print_tree(node.right, lines, level + 1)


def main():
    tree = RBTree()
    for x in range(1, 101):
        tree.insert(x)
    tree.delete(44)
    tree.delete(45)
    print(tree)

    print(4 * '\n')

    w_t = RBTree()
    for w in whiskey:
        w_t.insert(w)
    print(w_t)

    found = w_t.search('Woodford Reserve')
    if found:
        print(found.parent.item)
        print(found.left.item)
        print(found.right.item)


if __name__ == "__main__":
    main()
