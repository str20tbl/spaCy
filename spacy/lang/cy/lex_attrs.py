from __future__ import unicode_literals

from ...attrs import LIKE_NUM

# from ...attrs import IS_MUT

# Angen deall sut i drin rhifau aml-air
# Angen rhifau benywaidd
_num_words = ['sero', 'un', 'dau', 'tri', 'pedwar', 'pump', 'chwech', 'saith',
              'wyth', 'naw', 'deg', 'deuddeg',
              'pymtheg', 'deunaw', 'ugain',
              'deugain', 'trigain',
              'can', 'cant', 'mil', 'miliwn', 'biliwn', 'triliwn', 'cwadriliwn',
              'gajiliwn', 'basiliwn']

ordinals = [
    "cyntaf", "ail", "trydydd", "pedwerydd", "pumed", "chweched", "seithfed", "wythfed", "nawfed", "degfed",
    "un ar ddegfed", "deuddegfed", "un deg tri", "un deg pedwar", "pymthegfed", "un deg chwech", "un deg saith",
    "deunawfed", "un deg naw", "ugeinfed", "dau ddeg un", "dau ddeg dau", "dau ddeg tri", "dau ddeg pedwar",
    "dau ddeg pump", "dau ddeg chwech", "dau ddeg saith", "dau ddeg wyth", "dau ddeg naw", "tri deg", "tri deg un"
]

short_ordinal = [
    "fed", "ail", "ydd"
]


def like_num(token):
    text = str(token).lower()
    print(">>>>>>>>>>>>", text)
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text in ordinals:
        return True
    if text in _num_words:
        return True
    for sh in short_ordinal:
        if sh in text:
            return True
    return False


LEX_ATTRS = {
    LIKE_NUM: like_num
}
