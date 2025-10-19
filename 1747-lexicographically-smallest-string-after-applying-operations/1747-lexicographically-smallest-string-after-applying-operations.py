class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        smallest = s

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            smallest = min(smallest, cur)

            s_list = list(cur)
            for i in range(1, len(s_list), 2):
                s_list[i] = str((int(s_list[i]) + a) % 10)
            added = ''.join(s_list)

            rotated = cur[-b:] + cur[:-b]

            if added not in seen:
                q.append(added)
            if rotated not in seen:
                q.append(rotated)

        return smallest
        