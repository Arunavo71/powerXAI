from powerxai.types import Set, List
from itertools import combinations

def coalitions(player_set: Set[int]) -> List[Set[int]]:
    return [set(subset) for subset_size in range(len(player_set) + 1)
            for subset in combinations(player_set, subset_size)]