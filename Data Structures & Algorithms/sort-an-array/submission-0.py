class Solution:

    def merge(self, ar, s, m, e):
        l = e - s + 1
        temp = [0 for i in range(l)]
        i1 = s
        i2 = m + 1
        for i in range(l):
            if i1 <= m and i2 <= e:
                if ar[i1] <= ar[i2]:
                    temp[i] = ar[i1]
                    i1 += 1
                else:
                    temp[i] = ar[i2]
                    i2 += 1
            elif i1 <= m:
                temp[i] = ar[i1]
                i1 += 1
            else:
                temp[i] = ar[i2]
                i2 += 1
        for i in range(l):
            ar[s + i] = temp[i]

    def sort(self, ar, s, e):
        if e - s == 1:
            if ar[e] < ar[s]:
                ar[s], ar[e] = ar[e], ar[s]
        elif e - s > 1:
            m = s + ((e - s) // 2)
            self.sort(ar, s, m)
            self.sort(ar, m + 1, e)
            self.merge(ar, s, m, e)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums) - 1)
        return nums