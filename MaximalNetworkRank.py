class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = {}
        direct = {}
        
        for road in roads:
            count[road[0]] = count.get(road[0], 0) + 1
            count[road[1]] = count.get(road[1], 0) + 1
            direct[(road[0], road[1])] = 1
            direct[(road[1], road[0])] = 1
        
        rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = max(rank, count.get(i, 0) + count.get(j, 0) - direct.get((i, j), 0))
        
        return rank
