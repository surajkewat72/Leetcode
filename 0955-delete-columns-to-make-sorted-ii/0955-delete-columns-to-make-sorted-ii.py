class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        sorted_pair = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            bad = False
            for i in range(1, n):
                if not sorted_pair[i - 1] and strs[i][col] < strs[i - 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            for i in range(1, n):
                if not sorted_pair[i - 1] and strs[i][col] > strs[i - 1][col]:
                    sorted_pair[i - 1] = True

        return deletions
        