class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        # cycle detection
        visiting = set()
        # end condition of curr path
        visited = set()
        # the graph
        # course with no prereq == []
        prereq = defaultdict(list)
        for course, depended_course in prerequisites:
            prereq[course].append(depended_course)
        # dfs
        def dfs(course):
            if course in visited:
                return True
            # cycle detection
            if course in visiting:
                return False

            visiting.add(course)

            for req_course in prereq[course]:
                if not dfs(req_course):
                    return False
                visiting.discard(req_course)

            # when next recur returns true, append ret
            visited.add(course)
            ret.append(course)
            return True

        # iterating through all courses
        for curr_course in range(numCourses):
            if not dfs(curr_course):
                return []
            visiting.discard(curr_course)
        
        return ret
