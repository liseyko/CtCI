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

def _isBT_BST_2(btn, t_min = float('-inf'), t_max = float('inf')):
    #print(t_min,'<',btn.key,'<',t_max)
    if btn.key <= t_min or btn.key > t_max:
        return False
    l,r = True, True
    if btn.l:
        l = _isBT_BST_2(btn.l, t_min, btn.key)
    if btn.r:
        r = _isBT_BST_2(btn.r, btn.key, t_max)
    return l and r


def isBT_BST_2(t):
    if not t.root:
        return False
    return _isBT_BST_2(t.root, float('-inf'), float('inf'))


if __name__ == '__main__':
    t = AVLTree([1,2,3,4,5,6,7])
    print(isBT_BST(t))
    print(isBT_BST_2(t))

    t.root.l.r.key=5
    print(isBT_BST(t))
    print(isBT_BST_2(t))