class TimeMap:
    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return None
        values = self.data[key]
        i = bisect.bisect(values, (timestamp, chr(255)))
        return values[i-1][1] if i else ""
