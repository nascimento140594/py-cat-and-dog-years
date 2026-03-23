import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 24, [3, 2]),
        (24, 29, [2, 3]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        (-10, 24, [0, 2]),
        (24, -10, [2, 0]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        ("24", "24"),
    ],
)
def test_get_human_age_invalid_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
