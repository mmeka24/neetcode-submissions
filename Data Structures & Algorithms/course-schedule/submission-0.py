class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0] * numCourses

        for a,b in prerequisites:
            # pointing b to a 
            # so adj list of b should append a 
            adj[b].append(a)
            # indegree of a increments 
            indeg[a] += 1 

        q = deque()

        for i in range(numCourses): 
            if indeg[i] == 0:
                q.append(i)

        
        courses = 0 
        while q: 
            node = q.popleft()
            courses += 1
            for adj_node in adj[node]:
                # we just removed one of the in degrees 
                indeg[adj_node] -= 1 
                if indeg[adj_node] == 0:
                    q.append(adj_node)

        return courses == numCourses

        
