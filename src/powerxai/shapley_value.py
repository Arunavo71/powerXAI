from math import factorial
from powerxai.types import Callable, Set
from powerxai.coalitions import coalitions



def shapley_value(player_index: int,
                  num_players: int,
                  value_function: Callable[[Set[int]], float]
                  ) -> float:
    """
    Compute the Shapley value for a given player in a cooperative game.

    The Shapley value quantifies a player's average marginal contribution 
    across all possible coalitions.

    Args:
        player (int): The index of the player whose Shapley value is computed.
        num_players (int): The total number of players in the game.
        value_function (Callable[[Set[int]], float]): 
            A function that returns the value of any coalition (based on the player indices).

    Returns:
        float: The Shapley value of the specified player.
    """
    all_player_indices = set(range(num_players))
    total_value = 0.0
    for coalition in coalitions(all_player_indices - {player_index}):
        weight = (factorial(len(coalition)) * factorial(num_players - len(coalition) - 1)) / factorial(num_players)
        marginal_contribution = value_function(coalition | {player_index}) - value_function(coalition)
        total_value += weight * marginal_contribution

    return total_value