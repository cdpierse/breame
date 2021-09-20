# Breame

<p align="center"> ( <b>Br</b>itish <b>E</b>nglish and <b>Am</b>erican <b>E</b>nglish Language Tools) </p>

<h1 align="center"></h1>

<p align="center">
    <a href="https://opensource.org/licenses/Apache-2.0">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"/> 
    </a>
    <img src="./tests/static/coverage.svg">
    <a href="https://github.com/cdpierse/breame/releases">
        <img src="https://img.shields.io/pypi/v/breame?label=version"/> 
    </a>
</p>

Breame is a lightweight Python package with a number of utility tools to aid in the detection of words that have dual spellings in British and American English.

Breame can also be used to detect and provide definitions for words that have different meanings in both British English and American English.

Additionally, Breame includes some tooling to detect and define words and phrases that are specific to British English or American English i.e. "strop" in British English or "mailman" in American English.

## Install

```posh
pip install breame
```

# Documentation

## Quick Start

### Spelling Detection and Conversion

Check American and British English Spelling for words exists:

```python
from breame.spelling import american_spelling_exists, british_spelling_exists

american_spelling_exists("color")
>>> True
british_spelling_exists("colour")
>>> True
```

Get British English spelling of American English word and vice versa:

```python
from breame.spelling import get_american_spelling, get_british_spelling

get_american_spelling("colour")
>>> 'color'
get_british_spelling("color")
>>> 'colour'
```

### Detect different word meanings in British and American English

```python
from breame.meanings import different_meanings_exist, get_meaning_definitions

different_meanings_exist("football")
>>> True
get_meaning_definitions("football")
>>> {'American English': 'American football',
 'British English': '(usually) Association football (US: soccer). Less frequently applies to \nRugby football (espec. Rugby union in English private schools).'}
```

### Detect whether a word is a term or short phrase specific to American English or British English

American:

```python
from breame.terminology import is_american_english_term, get_american_term_definition

is_american_english_term("bleachers")
>>> True
get_american_term_definition("bleachers")
>>> 'are the raised open air tiered rows of seats (stands) found at sports fields or at other spectator events'
```

British:

```python
from breame.terminology import is_british_english_term, get_british_term_definition

is_british_english_term("wellies")
>>> True
get_british_term_definition("wellies")
>>> 'Wellington boots, waterproof rubber boots named after the Duke of Wellington.'
```

## Acknowlegments
