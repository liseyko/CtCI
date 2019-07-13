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
        self.numOfPeople = n
        self.knownPeopleOf = [set() for _ in range(n)]
        self.peopleWhoKnowsPerson = [set() for _ in range(n)]
        peopleWhoKnowNoOne = set()
        for pid in range(n):
            self.findAllKnownPeople(pid)
            if len(self.knownPeopleOf[pid]) == 0:
                peopleWhoKnowNoOne.add(pid)

        for pid in peopleWhoKnowNoOne:
            if len(self.peopleWhoKnowsPerson[pid]) == n-1:
                return pid

        return -1

    def findAllKnownPeople(self, pid):
        for anotherPid in range(self.numOfPeople):
            if anotherPid == pid:
                continue
            if knows(pid, anotherPid):
                self.knownPeopleOf[pid].add(anotherPid)
                self.peopleWhoKnowsPerson[anotherPid].add(pid)
