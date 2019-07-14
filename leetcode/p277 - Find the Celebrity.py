# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebrity = 0
        for person in range(1, n):
            if knows(celebrity, person):
                celebrity = person
        if any(knows(celebrity, person) for person in range(celebrity)):
            return -1
        if any(not knows(person, celebrity) for person in range(n)):
            return -1

        return celebrity

    def findCelebrity(self, n):
        potentialCelebrity = 0
        for person in range(1, n):
            if knows(potentialCelebrity, person):
                potentialCelebrity = person
        for person in range(potentialCelebrity):
            if knows(potentialCelebrity, person):
                return -1
        for person in range(n):
            if not knows(person, potentialCelebrity):
                return -1
        return potentialCelebrity


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        for person in range(n):
            if self.isPotentialCelebrity(person) and self.doesEverybodyKnow(person):
                return person
        return -1

    def isPotentialCelebrity(self, person):
        for anotherPerson in range(self.n):
            if person != anotherPerson and knows(person, anotherPerson):
                return False
        return True

    def doesEverybodyKnow(self, person):
        for anotherPerson in range(self.n):
            if not knows(anotherPerson, person):
                return False
        return True
