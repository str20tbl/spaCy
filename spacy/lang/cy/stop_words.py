# Set gychwynnol - angen gwneud hyn yn iawn
# encoding: utf8
from __future__ import unicode_literals

ADPS = set("""
â ag am ar at
dan dros drwy
gan gyda
heb
hyd
i
mewn
o
tros
wedi
wrth
ym
yn
yng
'n

arnaf
""".split())

ADVS = set("""
beth ble
llawer lle
yma yna
""".split())

AUXS = set("""
bod
mae
sy
sydd
yw

byddaf

ydwyf
""".split())

# Careful! Can also mean 'an age', 'a stone'
AMBIGS = set("""
oes
maen
""".split())

CONJS = set("""
a ac fel neu ond os tra
""".split())

DETS = set("""
y yr 'r
""".split())

NOUNS = set("""
ôl tu
""".split())

PARTS = set("""
na nid nis
""".split())

PRONS = set("""
di dy ef ei ein eich fe fy hwy hi i hun hyn ni nhw pob
""".split())

STOP_WORDS = set(ADPS | ADVS | AUXS | AMBIGS | CONJS | DETS | NOUNS | PARTS | PRONS)
