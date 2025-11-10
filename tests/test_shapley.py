from powerxai.shapley_value import shapley_value



def test_single_non_null_player():
    def value(players, coalition) -> float:
        """
        Value function.

        Args:
            coalition (Set[int]): Indices of players whose coalition value is computed.

        Returns:
            float: The coalitional value of the specified players.
        """
        player_coalition = [players[index] for index in coalition]
        if "Valuable Player" in player_coalition: return 1.0
        else:                                     return 0.0
    
    players = ["Null Player", "Null Player", "Null Player", "Valuable Player"]
    expected = [0.0, 0.0, 0.0, 1.0]
    num_players = len(players)
    result = [
        shapley_value(player_index=i, players=players, value_function=value)
        for i in range(num_players)
    ]
    assert result == expected


def test_asymmetric_contributions():
    def value(players, coalition) -> float:
        weights = {"A": 1, "B": 2, "C": 3}
        return float(sum(weights[players[i]] for i in coalition))
    
    players = ["A", "B", "C"]
    expected = [1.0, 2.0, 3.0]
    num_players = len(players)
    result = [
        shapley_value(player_index=i, players=players, value_function=value)
        for i in range(num_players)
    ]
    assert result == expected


def test_static_value_function():
    def static_value(players, coalition) -> float: return 1.0

    players = [1, 2, 3]
    expected = [0.0, 0.0, 0.0] # Since value is static everyone becomes a null-player.
    num_players = len(players)
    result = [
        shapley_value(player_index=i, players=players, value_function=static_value)
        for i in range(num_players)
    ]
    assert result == expected