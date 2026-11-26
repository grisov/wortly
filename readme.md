# Wortly

* Author: Oleksandr Gryshchenko
* Version: 0.0.1 (in development)
* NVDA compatibility: 2026.1 and beyond
* Download: [releases of the add-on][1]

Wortly helps blind and visually impaired people learn German words with NVDA. The add-on speaks a word in Ukrainian, and you type it in German. Learning is based on flashcards and spaced repetition: the words you get wrong come back more often, and the words you know well come back less often.

This is an early development version: the features of the add-on are being designed and are not available yet.

## Planned features
* Flashcards with spaced repetition: the words with mistakes are repeated more often.
* Word sets grouped by topics and levels, convenient for learning.
* Vocabulary dictations, filling in missing letters and other exercises.
* Pronunciation of German words, if a public audio service is available.
* Word sets and audio downloaded from one server, so the data stay in sync.

## Change log
The history of changes for each version of the add-on is published on the [Releases page][1] of the add-on repository.

## Altering of add-on source code
You may clone this repo to make alterations to Wortly.

Requirements:

* [uv](https://docs.astral.sh/uv/) - manages Python and all development tools of the add-on;
* [GNU Gettext tools](https://mlocati.github.io/articles/gettext-iconv-windows.html) (`msgfmt` and `xgettext` in the `PATH`) - compile translations and generate the template of translatable strings.

Run the following commands from the root of the repository:

1. `uv sync` - install the development dependencies;
2. `uv run prek run --all-files` - run all code checks: linting and formatting with ruff, type checking with pyright and other checks;
3. `uv run python -m unittest discover -s tests -v` - run the unit tests;
4. `uv run scons` - build the add-on, the created `.nvda-addon` file is placed in the root of the repository;
5. `uv run scons pot` - generate the `.pot` file with all translatable strings of the add-on (optional).

[1]: https://github.com/grisov/wortly/releases
