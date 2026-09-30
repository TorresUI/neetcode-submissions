class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        keyArray = self.timeMap[key]

        #we know this array is in order and that the first index of the tuple is the timezone.
        #We want the timezone to equal or the largest timezone
        res = ''
        maxNum = 0
        l, r = 0, len(keyArray) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            mTimestamp, mValue = keyArray[m]
            if mTimestamp == timestamp:
                res = mValue
                break
            elif mTimestamp > timestamp:
                r = m - 1
            else:
                res = mValue
                l = m + 1

        return res
