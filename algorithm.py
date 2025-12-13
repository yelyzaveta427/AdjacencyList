from typing import Dict, List

def hasHamiltonianPath(graph: Dict[int, List[int]]) -> bool:
    n = len(graph)
    if n == 0:
        return True
    max_states = 1 << n
    dp: List[List[bool]] = [[False] * n for _ in range(max_states)]

    for v in range(n):
        dp[1 << v][v] = True

    for mask in range(1, max_states):
        for v in range(n):
            if mask & (1 << v):
                prev_mask = mask ^ (1 << v)

                if prev_mask == 0:
                    continue


                for u in graph.get(v, []):
                    if (prev_mask & (1 << u)) and dp[prev_mask][u]:
                        dp[mask][v] = True
                        break

    full_mask = max_states - 1

    for v in range(n):
        if dp[full_mask][v]:
            return True

    return False