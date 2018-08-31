import sys

def get_perm_idxs(idx_set): # 1 2 3
    if len(idx_set) < 2:
        return [list(idx_set)]
    r = []
    for i in idx_set:
        r += [[i] + s for s in get_perm_idxs(idx_set-{i})]
    return r

def print_perms(s):
    for idx_list in get_perm_idxs({i for i in range(len(s))}):
        for i in idx_list:
            print(s[i], sep='', end='')
        print('', sep='', end=' ')
    print()
        

if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split()))[1:]
    for s in data:
        print_perms(sorted(s))
