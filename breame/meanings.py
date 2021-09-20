from breame.data.meaning_constants import DIFFERENT_MEANINGS_US_UK_COMMON
from breame.utils import process_word


def multiple_meanings_exist(word: str) -> bool:
    """
    Checks if the word has multiple meanings American, British, or Common English.
    Returns True if the word has multiple meanings, False otherwise.
    """
    word = process_word(word)
    if word in DIFFERENT_MEANINGS_US_UK_COMMON:
        return True
    return False


def get_meaning_definitions(word: str) -> dict:
    """
    Retrieves the multiple meaning definitions of a word. In some combination of
    American, British, and Common English. Returns a dictionary of the multiple meanings
    if they exist, otherwise returns an empty dictionary.
    """
    word = process_word(word)

    if word in DIFFERENT_MEANINGS_US_UK_COMMON:
        return DIFFERENT_MEANINGS_US_UK_COMMON[word]
    return {}
