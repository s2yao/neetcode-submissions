class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dp = defaultdict(list)

        for course, prereq in prerequisites:
            dp[course].append(prereq)

        curr_path = set() 
        def dfs(curr_course):
            if curr_course in curr_path:
                return False
            curr_path.add(curr_course)

            for prereq in dp[curr_course]:
                if not dfs(prereq):
                    return False
            
            curr_path.discard(curr_course)
            dp[curr_course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
