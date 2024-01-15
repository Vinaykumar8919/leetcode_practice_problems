class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        loser = dict()
        for w, l in matches:
            loser[w] = loser.get(w,0)
            loser[l] = loser.get(l, 0)+1
        for p, lc in loser.items():
            if lc==0:
                res[0].append(p)
            elif lc==1:
                res[1].append(p)
        res[0].sort()
        res[1].sort()
        return res
