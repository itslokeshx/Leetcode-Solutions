class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph=[ [] for i in range(numCourses) ]
        indegree=[0] * numCourses
        count=0

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        
        queue=deque()

        for i in range(len(indegree)):
            if(indegree[i]== 0):
                queue.append(i)
        
        while queue:
            removed=queue.popleft()
            count+=1

            for next_course in graph[removed]:
                indegree[next_course]-=1
                if(indegree[next_course] == 0):
                    queue.append(next_course)
            
        return count==numCourses
            
        