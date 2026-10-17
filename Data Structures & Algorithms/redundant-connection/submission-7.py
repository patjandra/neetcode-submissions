class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(1, len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = parents[n-1] # node n is at index n-1 in parents

            while p != parents[p-1]: # while parent of node n is not itself (not the root)
                parents[p-1] = parents[parents[p-1]-1]
                p = parents[p-1]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1-1] > rank[p2-1]:
                parents[p2-1] = p1
                rank[p1-1] += rank[p2-1]
            else:
                parents[p1-1] = p2
                rank[p2-1] += rank[p1-1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]