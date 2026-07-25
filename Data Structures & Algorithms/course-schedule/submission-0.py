class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisite -> courses that depend on it
        anti_req = {course: [] for course in range(numCourses)}
        dependency_count = [0] * numCourses

        for course, prerequisite in prerequisites:
            anti_req[prerequisite].append(course)
            dependency_count[course] += 1

        roots = []
        for course in range(numCourses):
            if dependency_count[course] == 0:
                roots.append(course)

        while roots:
            course = roots.pop()

            for depending_course in anti_req[course]:
                dependency_count[depending_course] -= 1

                if dependency_count[depending_course] == 0:
                    roots.append(depending_course)

            del anti_req[course]

        return len(anti_req) == 0