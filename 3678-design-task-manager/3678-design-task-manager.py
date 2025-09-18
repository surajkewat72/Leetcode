import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.taskMap = {}  # taskId -> (priority, userId)
        self.heap = []     # (-priority, -taskId, taskId, userId)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.taskMap:
            userId = self.taskMap[taskId][1]
            self.taskMap[taskId] = (newPriority, userId)
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]  # Lazy deletion

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId, userId = heapq.heappop(self.heap)
            if taskId in self.taskMap:
                realPriority, realUserId = self.taskMap[taskId]
                if realPriority == -priority and realUserId == userId:
                    del self.taskMap[taskId]  # remove executed task
                    return userId
        return -1
