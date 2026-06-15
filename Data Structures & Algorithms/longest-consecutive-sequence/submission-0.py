class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums = set(nums)
        # Mapeamos cada número a sí mismo en un diccionario para evitar problemas de memoria
        parent = {n: n for n in nums}
        size = {n: 1 for n in nums}
        max_len = 1

        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            nonlocal max_len
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                # Union by size
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                max_len = max(max_len, size[root_i])

        for n in nums:
            if n + 1 in nums:
                union(n, n + 1)
        
        return max_len


        


