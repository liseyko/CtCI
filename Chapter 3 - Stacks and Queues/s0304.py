from stack import Stack

class Hanoi():
    def __init__(self,n_of_disks = 0):
        self.towers =[Stack() for _ in range(3)]
        for i in range(n_of_disks,0,-1):
            self.towers[0].push(i)

    def add(self,d,t = 0):
        if t < 3 and (len(self.towers[t])==0 or d <= self.towers[t].peek()):
            self.towers[t].push(d)
        else:
            print(self)
            raise ValueError(f'Error placing disk {d} to tower {t+1}.')

    def move(self,src=0,dst=2,clen = None):
        buf = 3 - src - dst
        if clen is None:
            clen = len(self.towers[src])
        if clen > 0:
            self.move(src,buf,clen-1)
            self.add(self.towers[src].pop(),dst)
            #print(self)
            self.move(buf,dst,clen-1)

    def move1disk(self,src,dst):
        sd=self.towers[src].peek()
        dd=self.towers[dst].peek()
        if sd is not None and (dd is None or sd <= dd):
            self.add(self.towers[src].pop(),dst)
            return True
        else:
            return False

    def move1diskEitherWay(self,src,dst):
        if not self.move1disk(src,dst):
            self.move1disk(dst,src)

    def isSolved(self,src,buf,dst):
        if len(self.towers[src]) == 0 and \
           len(self.towers[buf]) == 0:
            return True
        else:
            return False


    def iterSol(self,src,dst):
        buf = 3-src-dst
        if len(self.towers[src]) % 2 == 0:
            while not self.isSolved(src,buf,dst):
                self.move1diskEitherWay(src,buf)
                self.move1diskEitherWay(src,dst)
                if self.isSolved(src,buf,dst):
                    break
                self.move1diskEitherWay(buf,dst)
        else:
            while not self.isSolved(src,buf,dst):
                self.move1diskEitherWay(src,dst)
                if self.isSolved(src,buf,dst):
                    break
                self.move1diskEitherWay(src,buf)
                self.move1diskEitherWay(buf,dst)

    def __str__(self):
        return str([str(s) for s in self.towers])
