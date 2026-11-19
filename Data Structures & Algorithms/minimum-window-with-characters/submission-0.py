class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}

        have = 0
        need = len(countT)

        l = 0
        res = ""
        minLen = float("inf")

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]

                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                l += 1

        return res