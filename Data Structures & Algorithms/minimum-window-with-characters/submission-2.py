class Solution:
    def ord_to_i(self, c):
        i = ord(c) - ord('A')
        if ord(c) >= ord('a'):
            i = ord(c) - ord('a') + 26
        return i

    def substr(self, f_s, f_t):
        for i in range(len(f_t)):
            if f_s[i] < f_t[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        freq_s = [0] * (26 * 2)
        freq_t = [0] * (26 * 2)

        for c in t:
            i = self.ord_to_i(c)
            freq_t[i] += 1

        i = 0
        j = 0
        short_i = 0
        short_j = 10000
        # s[i:j] is a substring of t
        # s[short_i:short_j] is a best solution found yet
        while j < len(s):
            while j < len(s) and not self.substr(freq_s, freq_t):
                freq_s[self.ord_to_i(s[j])] += 1
                j += 1
            
            if not self.substr(freq_s, freq_t):
                break
            
            if j - i < short_j - short_i:
                short_i = i
                short_j = j

            freq_s[self.ord_to_i(s[i])] -= 1
            i += 1

        changed = False 
        while i < len(s) and self.substr(freq_s, freq_t):
            freq_s[self.ord_to_i(s[i])] -= 1
            i += 1
            changed = True
        if changed:
            i -= 1
            if j - i < short_j - short_i:
                short_i = i
                short_j = j

        if short_j - short_i > 1001:
            return ""

        return s[short_i:short_j]