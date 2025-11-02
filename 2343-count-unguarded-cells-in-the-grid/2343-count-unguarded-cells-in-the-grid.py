class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guard_set = {(r, c) for r, c in guards}
        wall_set = {(r, c) for r, c in walls}
        guarded = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and (nr, nc) not in wall_set and (nr, nc) not in guard_set:
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc

        total = m * n
        occupied = len(guard_set) + len(wall_set)
        return total - occupied - len(guarded)
        