class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dp = defaultdict(list)

        for course, prereq in prerequisites:
            dp[course].append(prereq)

        curr_path = set()
        complete = set()
        ret = []

        def dfs(curr_course):
            if curr_course in curr_path:
                return False
            if curr_course in complete:
                return True

            curr_path.add(curr_course)

            for prereq in dp[curr_course]:
                if not dfs(prereq):
                    return False
            
            curr_path.discard(curr_course)
            dp[curr_course] = []
            complete.add(curr_course)
            ret.append(curr_course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        print(ret)
        return ret