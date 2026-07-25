class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        visited, visiting = set(), set()
        prereq = defaultdict(list)
        for course, course_prereq in prerequisites:
            prereq[course].append(course_prereq)

        # dfs
        # update visiting
        # stop when current course if
            # cycle - return False
            # visited globally - append to ret return True
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for need in prereq[course]:
                if not dfs(need):
                    return False
            visiting.discard(course)
            visited.add(course)
            ret.append(course)
            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return []
        return ret



# num = 0
# visited = 
# visiting = 
# prereq = {
#     1: 0
# }
