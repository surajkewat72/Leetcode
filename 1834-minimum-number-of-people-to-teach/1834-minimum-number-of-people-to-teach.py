class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        lang_sets = [set(l) for l in languages]

        candidates = set()
        for u, v in friendships:
            u -= 1  
            v -= 1
            if lang_sets[u].isdisjoint(lang_sets[v]):  
                candidates.add(u)
                candidates.add(v)

        if not candidates:
            return 0  

        min_teach = float("inf")
        for L in range(1, n + 1):
            teach_count = 0
            for user in candidates:
                if L not in lang_sets[user]:
                    teach_count += 1
            min_teach = min(min_teach, teach_count)

        return min_teach
        