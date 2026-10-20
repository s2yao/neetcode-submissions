class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dep = defaultdict(list)

        tickets.sort(reverse=True)
        for start, end in tickets:
            dep[start].append(end)
        

        ret = []
        curr = ['JFK']

        while curr:
            curr_airport = curr[-1]
            if not dep[curr_airport]:
                ret.append(curr.pop())
            else:
                curr.append(dep[curr_airport].pop())
        
        return ret[::-1]