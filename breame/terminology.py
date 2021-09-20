from breame.data.american_terms_constants import AMERICAN_ENGLISH_ONLY_TERMS
from breame.data.british_terms_constants import BRITISH_ENGLISH_ONLY_TERMS
from breame.utils import process_word


def is_british_english_term(word: str) -> bool:
    """
    Returns True if the word is a British English specific term, False otherwise.
    """
    word = process_word(word)
    return word in BRITISH_ENGLISH_ONLY_TERMS


def is_american_english_term(word: str) -> bool:
    """
    Returns True if the word is an American English specific term, False otherwise.
    """
    word = process_word(word)
    return word in AMERICAN_ENGLISH_ONLY_TERMS


def get_british_term_definition(word: str) -> str:
    """
    Returns the British English definition of the word.
    """
    word = process_word(word)
    return BRITISH_ENGLISH_ONLY_TERMS[word]


def get_american_term_definition(word: str) -> str:
    """
    Returns the American English definition of the word.
    """
    word = process_word(word)
    return AMERICAN_ENGLISH_ONLY_TERMS[word]
