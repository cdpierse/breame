from breame.data.spelling_constants import (
    AMERICAN_ENGLISH_SPELLINGS,
    BRITISH_ENGLISH_SPELLINGS,
)
from breame.utils import process_word


def get_british_spelling(word: str) -> str:
    """
    Get the British spelling of an American English word.
    """
    word = process_word(word)
    if word not in AMERICAN_ENGLISH_SPELLINGS:
        return word
    return AMERICAN_ENGLISH_SPELLINGS[word]


def get_american_spelling(word: str) -> str:
    """
    Get the American spelling of a British English word.
    """
    word = process_word(word)
    if word not in BRITISH_ENGLISH_SPELLINGS:
        return word
    return BRITISH_ENGLISH_SPELLINGS[word]


def american_spelling_exists(word: str) -> bool:
    """
    Check if an American English spelling exists.
    """
    word = process_word(word)
    return word in AMERICAN_ENGLISH_SPELLINGS


def british_spelling_exists(word: str) -> bool:
    """
    Check if a British English spelling exists.
    """
    word = process_word(word)
    return word in BRITISH_ENGLISH_SPELLINGS
