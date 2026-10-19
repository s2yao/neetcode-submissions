class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        course_dep = defaultdict(list)

        for course, prereq in prerequisites:
            course_dep[prereq].append(course)
            indegree[course] += 1
        
        stack = []
        for course in range(numCourses):
            if course not in indegree:
                stack.append(course)
        
        complete = 0
        while stack:
            curr_course = stack.pop()
            complete += 1
            for next_course in course_dep[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] < 1:
                    stack.append(next_course)
        
        return complete == numCourses
            