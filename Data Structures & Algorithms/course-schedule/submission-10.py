class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dp = defaultdict(list)
        # seed the dp with dependencies
        for course, prereq in prerequisites:
            dp[course].append(prereq)

        # records visited courses in current path
        visiting = set()
        # validate if current course is valid
        def dfs(course):
            if course in visiting:
                return False
            if dp[course] == []:
                return True

            visiting.add(course)
            for prereq in dp[course]:
                prereq_result = dfs(prereq)
                if not prereq_result:
                    return False
            visiting.discard(course)
            dp[course] = []
            return True

        # iterate through all the courses
        for num in range(len(prerequisites)):
            if not dfs(num):
                return False
        
        return True
