# coding: utf8
from __future__ import unicode_literals

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups

from ...lookups import Lookups
from .lemmatizer import WelshLemmatizer

class WelshDefaults(Language.Defaults):
    #lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    #lex_attr_getters[LANG] = lambda text: "cy"
    #lex_attr_getters[NORM] = add_lookups(
    #    Language.Defaults.lex_attr_getters[NORM], BASE_NORMS
    #)
    #lex_attr_getters.update(LEX_ATTRS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS

    @classmethod
    def create_lemmatizer(cls, nlp=None, lookups=None):
        if lookups is None:
            lookups = Lookups()
        return WelshLemmatizer(lookups)


class Welsh(Language):
    lang = "cy"
    Defaults = WelshDefaults


__all__ = ["Welsh"]
