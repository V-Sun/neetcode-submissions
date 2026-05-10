class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        visited = set()
        
        for course, prereq in prerequisites:
            adjMap[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            if adjMap[course] == []:
                return True
            
            visited.add(course)
            for n in adjMap[course]:
                if dfs(n) is False:
                    return False
            visited.remove(course)
            adjMap[course] = []
            return True
        
        for n in range(numCourses):
            if dfs(n) is False:
                return False

        return True