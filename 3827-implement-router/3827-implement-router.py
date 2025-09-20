from collections import deque, defaultdict
import bisect
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.seen = set()    
        self.dest_map = defaultdict(list) 

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.seen:
            return False

        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_time = self.queue.popleft()
            self.seen.remove((old_src, old_dst, old_time))

            arr = self.dest_map[old_dst]
            idx = bisect.bisect_left(arr, old_time)
            if idx < len(arr) and arr[idx] == old_time:
                arr.pop(idx)
            if not arr:
                del self.dest_map[old_dst]

        self.queue.append(packet)
        self.seen.add(packet)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        self.seen.remove((src, dst, ts))

        arr = self.dest_map[dst]
        idx = bisect.bisect_left(arr, ts)
        if idx < len(arr) and arr[idx] == ts:
            arr.pop(idx)
        if not arr:
            del self.dest_map[dst]

        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        arr = self.dest_map[destination]
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)
        return right - left
