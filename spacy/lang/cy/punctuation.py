# coding: utf-8

from __future__ import unicode_literals
from ..punctuation import TOKENIZER_SUFFIXES

_cy_suffixes_lower = ["'ch", "'i", "'m", "'n", "'r", "'th", "'u", "'w"]
_cy_suffixes_upper = [s.upper() for s in _cy_suffixes_lower]
_cy_suffixes_lower_curly = [s.replace("'", "’") for s in _cy_suffixes_lower]
_cy_suffixes_upper_curly = [s.upper() for s in _cy_suffixes_lower_curly]

_cy_suffixes = _cy_suffixes_lower + _cy_suffixes_upper \
               + _cy_suffixes_lower_curly + _cy_suffixes_upper_curly

TOKENIZER_SUFFIXES = TOKENIZER_SUFFIXES + _cy_suffixes
