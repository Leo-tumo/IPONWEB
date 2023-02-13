NIL = None


def inorder_tree_walk(x):
    if x is not NIL:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


class Node:

    def __init__(self, k=NIL):
        self.parent = NIL
        self.right = NIL
        self.left = NIL
        self.key = k

    def traverse_infix(self, result=None):
        if result is None:
            result = []

        if self.left:
            self.left.traverse_infix(result)

        result.append(self.key)

        if self.right:
            self.right.traverse_infix(result)

        return result


class BST:

    def __init__(self):
        self.root = NIL

    def __repr__(self):
        if self.root == NIL:
            return 'BST is empty'
        return str(self.root.traverse_infix())

    def insert(self, new):
        z = Node(new)
        x = self.root
        y = NIL
        while x != NIL:
            y = x
            try:
                if z.key < x.key:
                    x = x.left
                else:
                    x = x.right
            except TypeError:
                raise TypeError("Tree can't contain different types")
        z.parent = y
        if y == NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u: Node, v: Node):
        if u.parent == NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != NIL:
            v.parent = u.parent

    def delete(self, dl):
        z = self.search(self, dl)
        if z == NIL:
            return
        if z.left == NIL:
            self.transplant(z, z.right)
        elif z.right == NIL:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y != z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    @staticmethod
    def search(self, k):
        x = self.root
        try:
            while x != NIL and k != x.key:
                if k < x.key:
                    x = x.left
                else:
                    x = x.right
            return x
        except TypeError:
            raise TypeError("Tree can't contain different types")

    @staticmethod
    def minimum(x):
        while x.left != NIL:
            x = x.left
        return x

    @staticmethod
    def maximum(x):
        while x.righ != NIL:
            x = x.right
        return x

    def successor(self, x):
        if x.right != NIL:
            return self.minimum(x.right)
        else:
            y: Node = x.parent
            while y != NIL and x == y.right:
                x = y
                y = y.parent
            return y

    def predecessor(self, x):
        if x.left != NIL:
            return self.maximum(x.left)
        else:
            y: Node = x.parent
            while y != NIL and x == y.left:
                x = y
                y = y.parent
            return y


whiskey = [
    'Jack Daniel\'s',
    'Jim Beam',
    'Johnnie Walker',
    'Glenfiddich',
    'Macallan',
    'Bulleit',
    'Maker\'s Mark',
    'Jameson',
    'Chivas Regal',
    'Crown Royal',
    'The Glenlivet',
    'Talisker',
    'Oban',
    'Lagavulin',
    'Laphroaig',
    'Bushmills',
    'Highland Park',
    'Glenmorangie',
    'The Macallan',
    'The Famous Grouse',
    'J & B Rare',
    'Dewar\'s',
    'Black Bottle',
    'Islay Mist',
    'Cutty Sark',
    'Wild Turkey',
    'Four Roses',
    'Suntory Yamazaki',
    'Nikka Yoichi',
    'Knob Creek',
    'Woodford Reserve',
    'Booker\'s',
    'Makers 46',
    'Evan Williams',
]

if __name__ == "__main__":
    bst = BST()
    for p in whiskey:
        bst.insert(p)

    # bst.insert('88')

    print(bst)
