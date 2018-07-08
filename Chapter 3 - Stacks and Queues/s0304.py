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

    def __str__(self):
        return str([str(s) for s in self.towers])
