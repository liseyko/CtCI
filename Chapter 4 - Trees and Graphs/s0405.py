from avltree import AVLTree


def get_r_parent(btn): # right parent, i.e. cur node should be a left child
    while btn.parent and btn.parent.r == btn:
        btn = btn.parent
    return btn.parent

def find_next(btn):
    if not btn:
        return None
    if btn.r:
        next = btn.r
        while next.l:
            next = next.l
    else:
        next = get_r_parent(btn)
    return next

def isBT_BST(t):
    if not t.root:
        return False
    a = t.root
    while a.l:
        a = a.l
    b = find_next(a)
    if not b:
        return True
    while b is not None:
        #print(a.key)
        if a.key > b.key:
            return False
        a, b = b, find_next(b)
    return True

if __name__ == '__main__':
    t = AVLTree([1,2,3,4,5,6,7])
    print(isBT_BST(t))

    t.root.l.r.key=5
    print(isBT_BST(t))
