class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #build adjancylist

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        
        count = 0
        visit = set()


        # def dfs(node):
        #     for nei in adj[node]:
        #         if nei not in visit:
        #             visit.add(nei)
        #             dfs(nei)
        #
        # for i in range(n):
        #     if i not in visit:
        #         visit.add(i)
        #         dfs(i)
        #         count += 1

        for i in range(n):
            if i in visit:
                continue
            visit.add(i)
            stack=[i]
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        stack.append(nei)
            count +=1

        return count

            