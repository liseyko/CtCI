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
