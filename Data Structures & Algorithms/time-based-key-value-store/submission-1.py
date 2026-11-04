class TimeMap:

    def __init__(self):
        self.key_arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_arr.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.key_arr.get(key)
        ret = ""
        if arr:
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m][0] == timestamp:
                    return arr[m][1]
                elif arr[m][0] > timestamp:
                    r = m - 1
                else:
                    ret = arr[m][1]
                    l = m + 1
        return ret
        
