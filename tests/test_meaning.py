from breame.data.meaning_constants import DIFFERENT_MEANINGS_US_UK_COMMON
from breame.meanings import different_meanings_exist, get_meaning_definitions


def test_different_meanings_exist():
    for meaning in DIFFERENT_MEANINGS_US_UK_COMMON:
        assert different_meanings_exist(meaning)


def test_different_meanings_exist_empty():
    assert not different_meanings_exist("house")


def test_get_meaning_definitions():
    for meaning in DIFFERENT_MEANINGS_US_UK_COMMON:
        assert get_meaning_definitions(meaning) != {}


def test_get_meaning_definitions_empty():
    assert get_meaning_definitions("test") == {}
