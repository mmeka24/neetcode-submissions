class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        visited = set()
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b) 
            adj[b].append(a) 
        
        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    # actually go there
                    dfs(nei)

            # if n in ivisted and neightbor is my parent ignore it 

        dfs(0)
        # must ensure all nodes are viisted 
        # valid tree needs all nodes to be visited 
        return len(visited) == n
        