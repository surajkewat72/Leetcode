class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
    
        knows = set([0, firstPerson])
        i = 0
        
        while i < len(meetings):
            time = meetings[i][2]
            
            graph = defaultdict(list)
            people_in_time = set()
            
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people_in_time.add(x)
                people_in_time.add(y)
                i += 1
            
            visited = set()
            
            for person in people_in_time:
                if person not in visited:
                    queue = deque([person])
                    component = set([person])
                    visited.add(person)
                    
                    while queue:
                        u = queue.popleft()
                        for v in graph[u]:
                            if v not in visited:
                                visited.add(v)
                                component.add(v)
                                queue.append(v)
                    
                    if component & knows:
                        knows |= component
        
        return list(knows)