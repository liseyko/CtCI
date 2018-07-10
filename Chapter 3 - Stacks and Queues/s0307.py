from queue import Queue

class Animal():
    animals = {}
    cntr = 0
    def __init__(self,id=None):
        if not self.animal_type:
            self.animal_type = "unspecified"
        if self.animal_type in Animal.animals:
            Animal.animals[self.animal_type] += 1
        else:
            Animal.animals[self.animal_type] = 1
        self.id = self.animal_type + str(Animal.animals[self.animal_type])
        self.priority = Animal.cntr
        Animal.cntr += 1

class Cat(Animal):
    def __init__(self):
        self.animal_type = "cat"
        super().__init__()


class Dog(Animal):
    def __init__(self):
        self.animal_type = "dog"
        super().__init__()



class AnimalNode():
    def __init__(self,animal):
        self.animal = animal
        self.next = None
        setattr(self, 'next_' + animal.animal_type, None)

class AnimalShelter():
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self,animal):
        cur_node = AnimalNode(animal)
        if animal.animal_type == "cat":
            return self.cats.enqueue(animal)
        elif animal.animal_type == "dog":
            return self.dogs.enqueue(animal)
        else:
            return False

    def dequeueAny(self):
        dogs_cnt = len(self.dogs)
        cats_cnt = len(self.cats)
        a_cnt = cats_cnt + dogs_cnt
        if a_cnt == 0:
            return False
        if min(cats_cnt, dogs_cnt) > 0:
            if self.cats.peek().priority < self.dogs.peek().priority:
                return self.cats.dequeue()
            else:
                return self.dogs.dequeue()
        elif cats_cnt == 0:
            return self.dogs.dequeue()
        elif dogs_cnt == 0:
            return self.cats.dequeue()

    def dequeueDog(self):
        return self.dogs.dequeue()

    def dequeueCat(self):
        return self.cats.dequeue()

    def show(self):
        print("cats:")
        for a in self.cats:
            print(a.data.id,end='->')
        print("\ndogs:")
        for a in self.dogs:
            print(a.data.id,end='->')
        print("\n\n")
