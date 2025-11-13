import math
from powerxai.coalitions import maximal_chains


def test_maximal_chains_empty_set():
    chains = maximal_chains(set())
    assert chains == [[set()]]


def test_maximal_chains_singleton_set():
    players = {1}
    chains = maximal_chains(players)
    assert len(chains) == math.factorial(len(players)) == 1
    assert len(chains[0]) == len(players) + 1 == 2
    assert chains[0][0] == set()
    assert chains[0][1] == players


def test_maximal_chains_three_element_set_structure():
    players = {1, 2, 3}
    chains = maximal_chains(players)
    assert len(chains) == math.factorial(len(players)) == 6

    for chain in chains:
        assert len(chain) == len(players) + 1 == 4
        assert chain[0] == set()
        assert chain[-1] == players

        for previous, current in zip(chain, chain[1:]):
            assert previous < current
            assert len(current) == len(previous) + 1