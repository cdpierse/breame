from breame.data.american_terms_constants import AMERICAN_ENGLISH_ONLY_TERMS
from breame.data.british_terms_constants import BRITISH_ENGLISH_ONLY_TERMS


def test_american_terms_have_non_empty_string_values():
    for term, value in AMERICAN_ENGLISH_ONLY_TERMS.items():
        assert value is not None


def test_british_terms_have_non_empty_string_values():
    for term, value in BRITISH_ENGLISH_ONLY_TERMS.items():
        assert value is not None


def test_american_terms_are_all_lower_case():
    for term, value in AMERICAN_ENGLISH_ONLY_TERMS.items():
        if term.isnumeric() or term[0].isnumeric():
            continue
        assert term.islower()


def test_british_terms_are_all_lower_case():
    for term, value in BRITISH_ENGLISH_ONLY_TERMS.items():
        if term.isnumeric() or term[0].isnumeric():
            continue
        assert term.islower()
