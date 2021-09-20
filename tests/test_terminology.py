from breame.data.american_terms_constants import AMERICAN_ENGLISH_ONLY_TERMS
from breame.data.british_terms_constants import BRITISH_ENGLISH_ONLY_TERMS
from breame.terminology import (
    get_american_term_definition,
    get_british_term_definition,
    is_american_english_term,
    is_british_english_term,
)


def test_all_british_terms_return_true_for_is_british_english_term():
    for term in BRITISH_ENGLISH_ONLY_TERMS:
        assert is_british_english_term(term)


def test_all_american_terms_return_true_for_is_american_english_term():
    for term in AMERICAN_ENGLISH_ONLY_TERMS:
        assert is_american_english_term(term)


def test_all_american_terms_return_false_for_is_british_english_term():
    for term in AMERICAN_ENGLISH_ONLY_TERMS:
        assert not is_british_english_term(term)


def test_all_british_terms_return_false_for_is_american_english_term():
    for term in BRITISH_ENGLISH_ONLY_TERMS:
        assert not is_american_english_term(term)


def test_all_british_terms_return_non_empty_string_definition_for_get_british_term_definition():
    for term in BRITISH_ENGLISH_ONLY_TERMS:
        assert get_british_term_definition(term) != ""


def test_all_american_terms_return_non_empty_string_definition_for_get_american_term_definition():
    for term in AMERICAN_ENGLISH_ONLY_TERMS:
        assert get_american_term_definition(term) != ""
