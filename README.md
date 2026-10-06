# PHAS0083, Statistical Analysis of Data: the scripts

The Python scripts printed in the lecture notes of PHAS0083, Statistical
Analysis of Data, taught by Matteo Agostini at University College London.
They are grouped by chapter and named after the example of the notes they
belong to: the script of Example 9.2.2 is `ch09/example_9.2.2.py`.

Each script is exactly as printed in the notes, after a comment line with
its example and figure and three lines that import `preamble.py`: the
imports, the random number generator with its seed and the colours that
every script assumes.

## Running a script

Download or clone the whole repository, then

```
pip install -r requirements.txt
python ch09/example_9.2.2.py
```

A script finds `preamble.py` at the top of the repository from any folder.
To run a script on its own, copy `preamble.py` beside it, or replace its
three import lines with the content of `preamble.py`.

The seed is fixed, so a script produces the numbers quoted in the notes;
change it to see how the results vary from one simulation to the next. The
plots look different from the notes, which draw them with their own sizes
and fonts.

The scripts are generated from the source of the notes: please report
problems rather than editing them here.
