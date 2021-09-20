from breame.data.spelling_constants import (
    AMERICAN_ENGLISH_SPELLINGS,
    BRITISH_ENGLISH_SPELLINGS,
)
from breame.spelling import (
    american_spelling_exists,
    british_spelling_exists,
    get_american_spelling,
    get_british_spelling,
)


def test_get_british_spelling_returns_expected_word():
    for k, v in AMERICAN_ENGLISH_SPELLINGS.items():
        assert get_british_spelling(k) == v


def test_get_american_spelling_returns_expected_word():
    for k, v in BRITISH_ENGLISH_SPELLINGS.items():
        assert get_american_spelling(k) == v


def test_american_spelling_exists_returns_true_for_valid_word():
    for k, v in AMERICAN_ENGLISH_SPELLINGS.items():
        assert american_spelling_exists(k)


def test_american_spelling_exists_returns_false_for_invalid_word():
    assert not american_spelling_exists("blah")


def test_british_spelling_exists_returns_true_for_valid_word():
    for k, v in BRITISH_ENGLISH_SPELLINGS.items():
        assert british_spelling_exists(k)


def test_british_spelling_exists_returns_false_for_invalid_word():
    assert not british_spelling_exists("blah")


def test_get_british_spelling_returns_words_identity_when_not_in_american_dict():
    assert get_british_spelling("blah") == "blah"


def test_get_american_spelling_returns_words_identity_when_not_in_british_dict():
    assert get_american_spelling("blah") == "blah"
