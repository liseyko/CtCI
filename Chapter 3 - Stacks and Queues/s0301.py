# use single array to implement 3 stacks
LEN_OF_ARRAY = 48
N_OF_STACKS = 3

class MemAlloc():
    """memory manager for using just 1 'array' for 3 stacks"""
    """TODO: deallocation"""
    mem = [0 for i in range(LEN_OF_ARRAY)]
    allocated = []
    allocated_size = 0
    stack_list = []

    def __init__(self,mem_size=LEN_OF_ARRAY // N_OF_STACKS,stack_id=None):
        if len(MemAlloc.allocated) < N_OF_STACKS and \
                MemAlloc.allocated_size + mem_size <= len(MemAlloc.mem):
            self.id=len(MemAlloc.allocated)
            self.size = mem_size
            self.loc = MemAlloc.allocated_size
            MemAlloc.allocated.append(self)
            MemAlloc.stack_list.append(stack_id)
            MemAlloc.allocated_size += mem_size
        else:
            #print(MemAlloc.allocated_size + mem_size,'?', len(MemAlloc.mem))
            print("mem alloc err")
            raise ValueError(f'Can not allocate more than {N_OF_STACKS} stacks ' \
                            f'or more than {LEN_OF_ARRAY} elements of data.')

    def shift(self,real_size,dst,left=True):
        if left: 
            r = (0,real_size,1)
        else:
            r = (real_size,-1,-1)
        for i in range(r[0],r[1],r[2]):
            MemAlloc.mem[dst + i] = MemAlloc.mem[self.loc + i]
        self.loc = dst


    def reallocate(self):
        n_of_stacks = len(MemAlloc.stack_list)
        sizes = [len(mem) for mem in MemAlloc.allocated]
        real_size = [len(stack) for stack in MemAlloc.stack_list]
        free_space = [sizes[i]-real_size[i] for i in range(len(sizes))]
        free_space_total = sum(free_space)
        if free_space_total < n_of_stacks*2-1:
            return False # not enough free space to bother
        
        new_free_space = [free_space_total // n_of_stacks for _ in range(n_of_stacks)]
        for i in range(n_of_stacks):
            if free_space[i] == 0:
                new_free_space[i]+=free_space_total % n_of_stacks
                break
        new_loc = [0]
        for i in range(1,n_of_stacks):
            new_loc.append(new_loc[i-1]+real_size[i-1]+new_free_space[i-1])
        print(sizes,'-',real_size,'=',free_space,'total:',free_space_total)
        print('new free space:',new_free_space,'new locations:', new_loc)

        if n_of_stacks == 3 and free_space[0] > free_space[2]:
            for i in range(1,n_of_stacks):
                MemAlloc.allocated[i].shift(real_size[i], new_loc[i])
        else:
            for i in range(n_of_stacks-1,0,-1):
                MemAlloc.allocated[i].shift(real_size[i], new_loc[i],left=False)


        for i in range(0,n_of_stacks):
            MemAlloc.allocated[i].size = real_size[i] + new_free_space[i]
        return True



    def __getitem__(self, key):
        if key < self.size:
            return MemAlloc.mem[self.loc + key]
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, key, item):
        if key < self.size:
            MemAlloc.mem[self.loc + key] = item
        else:
            raise IndexError("list index out of range")

    def __len__(self):
        return self.size


class StackInArray():
    """stack in array"""
    def __init__(self,data=[],mem_size=LEN_OF_ARRAY//N_OF_STACKS):
        #self.mem = [None for i in range(mem_size)]
        self.mem = MemAlloc(mem_size,self)
        self.top = 0
        self.bottom = 0
        self.len = 0
        for elem in data:
            self.push(elem)

    def push(self,data):
        if self.bottom >= len(self.mem):
            print("Warning: Out of memory.")
            print(MemAlloc.mem)
            if self.mem.reallocate():
                print("Data reallocated.")
                print(MemAlloc.mem)
            else:
                print("Not enough space to reallocate data.")
        self.mem[self.bottom] = data
        self.bottom += 1
        self.len += 1

    def pop(self):
        if self.top != self.bottom:
            self.bottom -= 1
            data = self.mem[self.bottom]
            self.len -= 1
            return data
        else:
            return None

    def __str__(self):
        return str([self.mem[i] for i in range(self.len)])

    def __len__(self):
        return self.len

class StacksInArray():
    """ stacks in array management class"""
    def __init__(self):
        pass

""" Test """
stack1 = StackInArray(['s','t','a','c','k',1])
stack = StackInArray([3,4,5,6,7,8,9])
stack0 = StackInArray(['a','b','c'])
#stack3 = StackInArray(['S','T','3'],5)
print(stack)

for i in range(10,21):
    stack.push(i)
    print(i,stack)
print("---")
while stack.len > 0:
    stack.pop()
    #print(stack.pop(),stack)

print(None == stack.pop())
print(MemAlloc.mem)
#"""