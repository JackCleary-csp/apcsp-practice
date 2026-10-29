import pytest
import game

# Replace this template with at least three tests per game function:
# def test_describe_the_case():
#     assert game.your_function(chosen_input) == expected_result



def test_random_strategy_in_range():
    for i in range(0, 100, 1):
        result = game.random_strategy()
        assert result == 0 or result == 1 or result == 2

def test_random_strategy_evenly_distributed():
    counts = [0, 0, 0]
    for i in range (0, 10000, 1):
        result = game.random_strategy()
        counts[result] += 1 
    assert counts == pytest.approx([3333, 3333, 3333], rel=0.05)
    

    


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
