class TimeMap:

    def __init__(self):
        self.timeStamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeStamp:
            self.timeStamp[key].append([timestamp, value])
        else:
            self.timeStamp[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timeStamp:
            return ""

        l, r = 0, len(self.timeStamp[key]) - 1
        currentMaxTime = -1
        res = ""
        while l <= r:
            m = l + ((r - l) // 2)
            mTime, mValue = self.timeStamp[key][m]

            if mTime <= timestamp:
                if mTime > currentMaxTime:
                    currentMaxTime = mTime
                    res = mValue

                l = m + 1
            else:
                r = m - 1
        
        return res

                    
