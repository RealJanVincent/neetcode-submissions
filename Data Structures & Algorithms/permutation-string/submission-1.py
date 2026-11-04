class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f = {}
        for c in s1:
            if c not in f:
                f[c] = 0
            f[c] += 1
        zeroes = 0
        # invariant s2[l:r] contains part permutation of s1
        # zeroes shows number of frequencies covered by s2[l:r]
        l = 0
        r = 0
        while r < len(s2):
            if zeroes == len(f):
                break
            else:
                c = s2[r]
                if c in f:
                    f[c] -= 1
                    if f[c] == 0:
                        zeroes += 1
                    if f[c] < 0:
                        # while l < r and f[c] < 0:
                        while f[c] < 0:
                            left_char = s2[l]
                            f[left_char] += 1
                            if f[left_char] == 1:
                                zeroes -= 1
                            l += 1
                else:
                    # move left
                    while l < r:
                        if f[s2[l]] == 0:
                            zeroes -= 1
                        f[s2[l]] += 1
                        l += 1
                    l += 1
                r += 1

        return zeroes == len(f)
