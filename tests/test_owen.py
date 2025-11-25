from powerxai.owen_value import owen_value
from .value_functions import (
    owen_three_person_game_example,
    owen_four_person_game_example,
)


def test_three_person_game_example_1_partition_1():
    players = [["A"], ["B"], ["C"]]
    num_players = sum(len(group) for group in players)
    expected = [63.3, 13.3, 23.3]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_three_person_game_example)
        for i in range(num_players)
    ]
    rounded = [round(x, 1) for x in result]
    assert rounded == expected


def test_three_person_game_example_1_partition_2():
    players = [["A", "B"], ["C"]]
    num_players = sum(len(group) for group in players)
    expected = [70.0, 20.0, 10.0]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_three_person_game_example)
        for i in range(num_players)
    ]
    assert result == expected


def test_three_person_game_example_1_partition_3():
    players = [["A", "C"], ["B"]]
    num_players = sum(len(group) for group in players)
    #            A     C     B
    expected = [70.0, 30.0, 0.0]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_three_person_game_example)
        for i in range(num_players)
    ]
    assert result == expected


def test_three_person_game_example_1_partition_4():
    players = [["A"], ["B", "C"]]
    num_players = sum(len(group) for group in players)
    expected = [50.0, 20.0, 30.0]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_three_person_game_example)
        for i in range(num_players)
    ]
    assert result == expected


def test_four_person_game_example_2_partition_1():
    players = [["A", "C"], ["B", "D"]]
    num_players = sum(len(group) for group in players)
    #            A     C     B     D
    expected = [30.0, 30.0, 20.0, 20.0]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_four_person_game_example)
        for i in range(num_players)
    ]
    assert result == expected


def test_four_person_game_example_2_partition_2():
    players = [["A", "C"], ["B"], ["D"]]
    num_players = sum(len(group) for group in players)
    #            A     C     B     D
    expected = [40.0, 33.3, 13.3, 13.3]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_four_person_game_example)
        for i in range(num_players)
    ]
    rounded = [round(x, 1) for x in result]
    assert rounded == expected


def test_four_person_game_example_2_partition_3():
    players = [["A", "B", "C"], ["D"]]
    num_players = sum(len(group) for group in players)
    expected = [41.7, 26.7, 31.7, 0]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_four_person_game_example)
        for i in range(num_players)
    ]
    rounded = [round(x, 1) for x in result]
    assert rounded == expected


def test_four_person_game_example_2_partition_4():
    players = [["A", "C", "D"], ["B"]]
    num_players = sum(len(group) for group in players)
    #            A     C     D    B
    expected = [38.3, 28.3, 33.3, 0]
    result = [
        owen_value(player_index=i, players=players, value_function=owen_four_person_game_example)
        for i in range(num_players)
    ]
    rounded = [round(x, 1) for x in result]
    assert rounded == expected