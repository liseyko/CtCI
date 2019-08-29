class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        shouldPrint = message not in self.d or timestamp - self.d[message] >= 10
        if shouldPrint:
            self.d[message] = timestamp
        return shouldPrint

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class Logger:
    def __init__(self):
        self.ts = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.ts.get(message, 0):
            return False
        self.ts[message] = timestamp + 10
        return True
