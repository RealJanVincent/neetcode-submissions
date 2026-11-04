class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_work = ""
        for c in s:
            if c.isalnum():
                to_work += c.lower()
                
        i = 0
        j = len(to_work) - 1
        while j > i:
            if to_work[i] != to_work[j]:
                return False
            i += 1
            j -= 1
        return True