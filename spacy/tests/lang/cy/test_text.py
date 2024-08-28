import pytest
import spacy
from spacy.lang.cy.lex_attrs import like_num


def test_cy_tokenizer_handles_long_text(cy_tokenizer):
    text = """Mae brechiadau’n eich amddiffyn rhag clefydau niweidiol cyn ichi ddod i gysylltiad â nhw. 
    Mae’r brechlyn yn galluogi eich system imiwnedd i greu gwrthgyrff mewn ffordd sy’n fwy diogel na 
    thrwy ddod i gysylltiad â’r clefyd ei hun.
    
    Nid yw brechiadau’n achosi’r clefyd nac yn eich rhoi mewn perygl o ddioddef y cymhlethdodau sy’n 
    gysylltiedig ag ef. Mae brechiadau’n cryfhau eich system imiwnedd 
    gan wella’ch gallu i wrthsefyll heintiau penodol."""
    tokens = cy_tokenizer(text)
    assert len(tokens) == 79


@pytest.mark.parametrize(
    "text,length",
    [
        ("Byddwn yn mynd am bryd o fwyd i ddathlu Dydd Sul y Tadau.", 14),
        ("Bydd rhyw ddeucant yn mynd i’r capel.", 8),
        ("“Mae ’i wallt o’n ’lyb.”", 10),
        ("""Gadawodd ar ei ôl""", 4),
        ("""'Os bydd angen i ni weithredu, fe wnawn', meddai.""", 14),
        ("Rho CF10 3AT yn y Sat-Nav.", 9),
        ("Mae'r gig yn dechrau am 20:00.", 7),
    ],
)
def test_cy_tokenizer_handles_cnts(cy_tokenizer, text, length):
    tokens = cy_tokenizer(text)
    assert len(tokens) == length


@pytest.mark.parametrize(
    "text,match",
    [
        ("10", True),
        ("1", True),
        ("10,000", True),
        ("10,00", True),
        ("999.0", True),
        ("un", True),
        ("dau", True),
        ("biliwn", True),
        ("ci", False),
        (",", False),
        ("1/2", True),
    ],
)
def test_lex_attrs_like_number(cy_tokenizer, text, match):
    tokens = cy_tokenizer(text)
    print(tokens[0])
    assert len(tokens) == 1
    assert like_num(tokens[0]) == match


@pytest.mark.parametrize(
    "word", ["trydydd", "pymthegfed", "10fed", "cyntaf", "23ydd", "52ail"]
)
def test_cy_lex_attrs_like_number_for_ordinal(word):
    assert like_num(word)


@pytest.mark.parametrize("word", ["deg"])
def test_cy_lex_attrs_capitals(word):
    assert like_num(word)
    assert like_num(word.upper())
