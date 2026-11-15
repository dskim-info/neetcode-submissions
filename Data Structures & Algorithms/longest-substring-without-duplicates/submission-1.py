class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0

        # for i in range(len(s)):
        #     charSet = set()

        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break

        #         charSet.add(s[j])

        #     res = max(res, len(charSet))

        # return res

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)

            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res