class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        Hash ={}
        res = 1
        for word in words:
            Max = 1
            for index in range(len(word)):
                new = word[:index]+word[index+1:]
                if new in Hash:
                    Max = max(Hash[new]+1, Max)
            Hash[word]=Max
            res = max(res, Max)
            # print(word, Hash[word])
        return max(list(Hash.values()))
