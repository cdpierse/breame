from breame.data.meaning_constants import DIFFERENT_MEANINGS_US_UK_COMMON

EXPECTED_KEY_NAMES = {"American English", "British English", "Common"}


def test_each_key_in_meanings_contains_at_least_one_key():
    """
    Test that each key in DIFFERENT_MEANINGS_US_UK_COMMON contains at least one key.
    """
    for key in DIFFERENT_MEANINGS_US_UK_COMMON:
        assert len(DIFFERENT_MEANINGS_US_UK_COMMON[key]) >= 1


def test_each_subkey_meanings_is_expected_key():
    """
    Test that each subkey in DIFFERENT_MEANINGS_US_UK_COMMON is expected key.
    """
    for key in DIFFERENT_MEANINGS_US_UK_COMMON:
        for subkey in DIFFERENT_MEANINGS_US_UK_COMMON[key]:
            assert subkey in EXPECTED_KEY_NAMES


def test_each_key_is_lowercase():
    """
    Test that each key in DIFFERENT_MEANINGS_US_UK_COMMON is lowercase.
    """
    for key in DIFFERENT_MEANINGS_US_UK_COMMON:
        assert key.islower()
