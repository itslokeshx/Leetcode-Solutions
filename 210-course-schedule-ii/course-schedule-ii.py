class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph= [ [] for i in range(numCourses)]
        indegree=[0] * numCourses
        op=[]

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        
        queue=deque()

        for i in range(numCourses):
            if(indegree[i] == 0):
                queue.append(i)

        while queue:
            removed=queue.popleft()
            op.append(removed)
            for next_courses in graph[removed]:
                indegree[next_courses]-=1
                if(indegree[next_courses] == 0):
                    queue.append(next_courses)
        
        if( len(op) == numCourses):
            return op
        else:
            return []
            
        
        