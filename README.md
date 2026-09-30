# PHAS0083, Statistical Analysis of Data: the scripts

The Python scripts printed in the lecture notes of PHAS0083 (University
College London, Matteo Agostini), one file per figure, grouped by chapter.
Each script is exactly as printed in the notes, after three lines that import
`preamble.py`, the preamble every script assumes (the imports, the random
number generator with its seed, the colours).

```
pip install -r requirements.txt
python ch09/example_9.2.2.py
```

A script finds `preamble.py` at the top of this repository from any folder;
to run one elsewhere, copy `preamble.py` beside it. The seed is fixed, so a
script produces the numbers quoted in the notes; change it to see how the
results vary from one simulation to the next. The plots look different from
the notes, which draw them with their own sizes and fonts.

The scripts are generated from the source of the notes: please report
problems rather than editing them here.
