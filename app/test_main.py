from app.main import get_human_age


def test_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_15_and_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_extra_rule() -> None:
    assert get_human_age(28, 24) == [3, 2]


def test_dog_extra_rule() -> None:
    assert get_human_age(24, 29) == [2, 3]


def test_no_extra_before_step() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
