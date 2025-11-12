from powerxai.upsilon_value import upsilon_value



def test_cardinality_measure():
    def cardinality_value(players, coalition) -> float:
        """
        Value function.

        Args:
            players (List[Any]): List of players or elements in the reference set.
            coalition (Set[int]): Indices of players whose coalition value is computed.

        Returns:
            float: The coalitional value of the specified players.
        """
        if len(coalition) == 1: return 1.0
        return 0.0
    
    players = ["A", "B", "C"]
    expected = [1.0, -1.0, 0.0]
    result = [
        upsilon_value(player_index=i, players=players, value_function=cardinality_value)
        for i in range(1, len(players)+1)
    ]
    assert result == expected


def test_static_measure():
    def static_value(players, coalition) -> float: return 1.0
    
    players = ["A", "B", "C"]
    expected = [0.0, 0.0, 0.0]
    result = [
        upsilon_value(player_index=i, players=players, value_function=static_value)
        for i in range(1, len(players)+1)
    ]
    assert result == expected


def test_single_valuable_player():
    def single_valuable(players, coalition) -> float:
        player_coalition = [players[index] for index in coalition]
        if "A" in player_coalition: return 1.0
        else:                       return 0.0
    
    players = ["A", "B", "C", "D"]
    expected = [0.25, 0.25, 0.25, 0.25]
    result = [
        upsilon_value(player_index=i, players=players, value_function=single_valuable)
        for i in range(1, len(players)+1)
    ]
    assert result == expected