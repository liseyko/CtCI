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

if __name__ == '__main__':
    t = AVLTree([1,2,3,4,5,6,7])
    n = t.root
    while n.l:
        n = n.l
    while n:
        print(n.key,end=',')
        n = find_next(n)

