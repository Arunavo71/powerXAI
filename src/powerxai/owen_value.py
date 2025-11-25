from math import factorial
from powerxai.types import Callable, Any
from powerxai.coalitions import coalitions


def owen_value(player_index: int,
               players: list[Any],
               value_function: Callable[[list[Any], set[int]], float],
               ) -> float:
    """
    Compute the Owen value for a given player in a cooperative game with
    a priori unions (group structure).

    We assume:
        - `players` may be a partitioned list of groups list[Any] or list[list[Any]]),
        each group being a list of atomic players.
        - Atomic players are referred to by their index in the flattened list of players.
        - `player_index` is an index in [0, total_number_of_atomic_players - 1].
        - `value_function(flattened_players, S)` returns v(S), where S is a set of
          atomic player indices in the flattened list.

    Args:
        player_index (int): Index of the atomic player whose Owen value is computed
            in the flattened players list.
        players (list[Any]): List of players (each player may be a group of atomic players: list[list[Any]]).
        value_function (Callable[[list[Any], set[int]], float]): 
            A function that returns the value of any coalition (based on the player indices).

    Returns:
        float: The Owen value of the specified player.
    """
    partition_indices: list[set[int]] = []
    current_index = 0
    for group in players:
        group_size = len(group)
        partition_indices.append(set(range(current_index, current_index + group_size)))
        current_index += group_size

    num_players = current_index
    assert 0 <= player_index < num_players, (f"player_index out of range. Must be in [0, {num_players - 1}]")

    group_index_of_player = next(index for index, group in enumerate(partition_indices) if player_index in group)

    num_groups = len(partition_indices)
    player_group = partition_indices[group_index_of_player]
    other_groups_indices = set(range(num_groups)) - {group_index_of_player}
    group_without_player = set(player_group) - {player_index}
    group_size = len(player_group)

    total_value = 0.0
    for indices_outer_coalition in coalitions(other_groups_indices):
        size_outer_coalition = len(indices_outer_coalition)
        weight_outer_coalition = (factorial(size_outer_coalition) *
                                  factorial(num_groups - size_outer_coalition - 1)) / factorial(num_groups)

        external_players = {player for idx in indices_outer_coalition for player in partition_indices[idx]}

        for inner_coalition in coalitions(group_without_player):
            size_inner_coalition = len(inner_coalition)
            weight_inner_coalition = (factorial(size_inner_coalition) *
                                      factorial(group_size - size_inner_coalition - 1)) / factorial(group_size)

            weight = weight_outer_coalition * weight_inner_coalition
            base_coalition = external_players | inner_coalition
            marginal_contribution = (
                value_function(players, base_coalition | {player_index}) -
                value_function(players, base_coalition)
            )

            total_value += weight * marginal_contribution

    return total_value