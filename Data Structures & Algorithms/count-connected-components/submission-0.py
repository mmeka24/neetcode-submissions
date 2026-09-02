class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Kosarajus algorithm 

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        components = 0

        for node in range(n): 
            # run bfs for every node in n nodes
            if node not in visited:
                components += 1 

                q = deque([node])
                visited.add(node)
                while q: 
                    cur = q.popleft()

                    for nei in adj[cur]:
                        if nei not in visited: 
                            q.append(nei)
                            visited.add(nei)

        return components


        
