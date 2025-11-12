from powerxai.types import Set, List
from itertools import combinations


def coalitions(player_set: Set[int]) -> List[Set[int]]:
    """
    Enumerate all coalitions (all subsets) of the given set of players.

    Args:
        player_set (Set[int]): Set of player indices.

    Returns:
        List[Set[int]]: A list of all subsets of player_set.
    """
    return [set(subset) for subset_size in range(len(player_set) + 1)
            for subset in combinations(player_set, subset_size)]


def maximal_chains(player_set: Set[int]) -> List[List[Set[int]]]:
    """
    Enumerate all maximal chains in the subset lattice 2^X for the given players.

    Args:
        player_set (Set[int]): Set of player indices.

    Returns:
        List[List[Set[int]]]: A list of maximal chains. Each chain is a list of length n+1. There are n! chains.
    """
    from itertools import permutations
    X = tuple(player_set)
    return [[set(permutation[:i]) for i in range(len(X)+1)] for permutation in permutations(X)]