import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_valid(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [-1, -10, -100])
def test_get_coin_combination_negative(cents: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize("cents", ["10", 5.5, None])
def test_get_coin_combination_invalid_type(cents: object) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
