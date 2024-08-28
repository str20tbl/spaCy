# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, NORM


TOKENIZER_EXCEPTIONS = {

    "a.y.y.b": [
        {ORTH: "a.", NORM: "ac"},
        {ORTH: "y.", NORM: "yn"},
        {ORTH: "y.", NORM: "y"},
        {ORTH: "b", NORM: "blaen"}
    ],

    "a.y.b": [
        {ORTH: "a.", NORM: "ac"},
        {ORTH: "y.", NORM: "yn y"},
        {ORTH: "b", NORM: "blaen"}
    ],

    "h.y.": [
        {ORTH: "h.", NORM: "hynny"},
        {ORTH: "y.", NORM: "yw"}
    ],

    "e.e.": [
        {ORTH: "e.", NORM: "er"},
        {ORTH: "e.", NORM: "enghraifft"}
    ],

    "A.C.": [
        {ORTH: "A.", NORM: "Aelod"},
        {ORTH: "C.", NORM: "Cynulliad"}
    ],

    "A.S.": [
        {ORTH: "A.", NORM: "Aelod"},
        {ORTH: "S.", NORM: "Seneddol"}
    ],

    "A.S.E.": [
        {ORTH:"A.", NORM: "Aelod"},
        {ORTH:"S.", NORM: "Seneddol"},
        {ORTH:"E.", NORM: "Ewropeaidd"}
    ],

    "g'ath": [{ORTH: "g'ath", NORM: "gafodd"}],

    "c'ath": [{ORTH: "c'ath", NORM: "gafodd"}]



}



# Times

for h in range(1, 12 + 1):
    for period in ["a.m.", "am"]:
        TOKENIZER_EXCEPTIONS["%d%s" % (h, period)] = [
            {ORTH: "%d" % h},
            {ORTH: period, NORM: "a.m."},
        ]
    for period in ["p.m.", "pm"]:
        TOKENIZER_EXCEPTIONS["%d%s" % (h, period)] = [
            {ORTH: "%d" % h},
            {ORTH: period, NORM: "p.m."},
        ]

for orth in [
    "'d",
    "a.m.",
    "Adm.",
    "Bros.",
    "co.",
    "Co.",
    "Corp.",
    "D.C.",
    "Dr.",
    "e.g.",
    "E.g.",
    "E.G.",
    "Gen.",
    "Gov.",
    "i.e.",
    "I.e.",
    "I.E.",
    "Inc.",
    "Jr.",
    "Ltd.",
    "Md.",
    "Messrs.",
    "Mo.",
    "Mont.",
    "Mr.",
    "Mrs.",
    "Ms.",
    "p.m.",
    "Ph.D.",
    "Prof.",
    "Rep.",
    "Rev.",
    "Sen.",
    "St.",
    "vs.",
    "v.s.",
]:
    TOKENIZER_EXCEPTIONS[orth] = [{ORTH: orth}]
