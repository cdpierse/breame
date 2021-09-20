import pytest
from breame.data.spelling_constants import (
    AMERICAN_ENGLISH_SPELLINGS,
    BRITISH_ENGLISH_SPELLINGS,
)


def test_spelling_keys_are_exclusive():
    "Asserts that no keys from either spelling dictionary are present in the other"
    assert (
        set(AMERICAN_ENGLISH_SPELLINGS.keys()).intersection(
            set(BRITISH_ENGLISH_SPELLINGS.keys())
        )
        == set()
    )

def test_spelling_keys_are_lowercase():
    "Asserts that all keys from either spelling dictionary are lowercase"
    assert (
        set(AMERICAN_ENGLISH_SPELLINGS.keys())
        == set(map(lambda x: x.lower(), AMERICAN_ENGLISH_SPELLINGS.keys()))
    )
    assert (
        set(BRITISH_ENGLISH_SPELLINGS.keys())
        == set(map(lambda x: x.lower(), BRITISH_ENGLISH_SPELLINGS.keys()))
    )