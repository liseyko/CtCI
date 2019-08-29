class Logger:
    def __init__(self):
        self.ts = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp < self.ts.get(message, 0):
            return False
        self.ts[message] = timestamp + 10
        return True


class Logger:

    def __init__(self):
        self.ts = {}
        self.h = []

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        def disablePrintingMsgUntil(n):
            self.ts[message] = n
            heapq.heappush(self.h, (n, message))

        def purgeStaleMsgBlocks():
            while self.h and self.h[0][0] < timestamp:
                oldest_msg = heapq.heappop(self.h)[1]
                if self.ts[oldest_msg] < timestamp:
                    del self.ts[oldest_msg]

        shouldBePrinted = timestamp > self.ts.get(message, -1)
        if shouldBePrinted:
            disablePrintingMsgUntil(timestamp+9)
            purgeStaleMsgBlocks()

        return shouldBePrinted
