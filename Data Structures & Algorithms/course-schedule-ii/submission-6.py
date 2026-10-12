class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dp = defaultdict(list)
        indegree = defaultdict(int)

        for course, prereq in prerequisites:
            dp[prereq].append(course)
            indegree[course] += 1

        stack = []

        for course in range(numCourses):
            if indegree[course] == 0:
                stack.append(course)
        
        ret = []
        while stack:
            curr_course = stack.pop()
            ret.append(curr_course)
            
            for prereq in dp[curr_course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    stack.append(prereq)
        
        if len(ret) != numCourses:
            return []
        return ret