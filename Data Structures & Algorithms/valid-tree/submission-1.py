class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set()
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b) 
            adj[b].append(a) 
        
        def dfs(node, parent):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    # actually go there
                    if not dfs(nei, node):
                        return False

                elif nei != parent:
                    # if neighbor is already visited and n is not my parent -> cycle
                    return False

            # if n in ivisted and neightbor is my parent ignore it 

            return True

        if len(edges) != n - 1:
            return False

        return dfs(0, -1) and len(visited) == n
        