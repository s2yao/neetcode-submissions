class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        fuck = defaultdict(list)
        degree = defaultdict(int)

        for course, prereq in prerequisites:
            fuck[prereq].append(course)
            degree[course] += 1
        
        stack = []
        for i in range(numCourses):
            if i not in degree:
                stack.append(i)
        complete = 0
        while stack:
            curr_course = stack.pop()
            complete += 1
            for dependent in fuck[curr_course]:
                degree[dependent] -= 1
                if degree[dependent] == 0:
                    stack.append(dependent)
        
        return complete == numCourses