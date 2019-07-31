"""
First keep going forward until you get stuck.
That's a good main path already.
Remaining tickets form cycles which are found on the way back
and get merged into that main path.
By writing down the path backwards when retreating from recursion,
merging the cycles into the main path is easy - the end part
of the path has already been written, the start part
of the path hasn't been written yet,
so just write down the cycle now and then keep backwards-writing the path.
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            targets[a].append(b)
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]
