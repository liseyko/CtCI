from btree import BTree

def is_btree_balanced(root):
    if not root:
        return False
    if root.l and root.r:
        return is_btree_balanced(root.l) and is_btree_balanced(root.r)
    elif not root.l and not root.r:
        return True
    else:
        if root.l:
            c = root.l
        else:
            c = root.r
        if c.l or c.r:
            return False
        return True


if __name__ == '__main__':

    t = BTree([5,3,8,10,7,4,1,8,13,11,12])
    print(is_btree_balanced(t.root))

    t = BTree([5,3,8])
    print(is_btree_balanced(t.root))

    t = BTree()
    print(is_btree_balanced(t.root))

