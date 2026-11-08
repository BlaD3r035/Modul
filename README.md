# Numeric Base Converter

Console app that converts a non-negative integer between decimal, binary, octal and
hexadecimal. You pick the source base, type the number, and the app shows it in all
four bases. It can also show the decimal-to-binary successive-division steps.

> UNAL MED Testing Class Project :)

## Features

- Menu with the four source bases and an exit option.
- Input validation: rejects symbols not in the base (`2` in binary, `G` in hex),
  accepts `A`-`F` in any case and leading zeros, rejects negatives/decimals, and
  rejects values over 1,000,000 (decimal).
- Converts to decimal (positional sum) and from decimal to each base (successive
  division). Hex is shown uppercase, no leading zeros.
- Optional decimal-to-binary step view (each division with quotient and remainder).
- Lists the session's conversions on exit.

## Structure

```
modul/
├── src/                       application code
│   ├── index.py               main menu and program flow
│   └── func/
│       ├── conversions.py     toDecimal / decimalTo (conversion logic)
│       ├── verify.py          input validation
│       └── prints.py          logo and menu
├── testing/
│   ├── blackbox_tests.ipynb   black-box tests (requirement-based)
│   └── whitebox_tests.ipynb   white-box tests (code-based)
└── README.md
```

`index.py` holds only the flow; all logic lives in `func`. Imports use
`from func... import ...`, so the app must run from `src/`.

## Requirements

- Python 3.10+ (uses `match`). No external dependencies.

## Run the app

```bash
cd src
python3 index.py
```

Pick a base (1-4) or exit (5), type the number, review the four bases, then answer
`y`/`n` to see the decimal-to-binary steps.

## Run the tests

Tests are Jupyter notebooks in `testing/` that import the real code from `src`, so
run them from that folder. Requires Jupyter (`pip install jupyter`).

From Jupyter — open a notebook and use **Restart Kernel & Run All**. The Setup cell
reloads the `src` modules; restart the kernel after changing app code.

```bash
cd testing
jupyter notebook
```

From the terminal:

```bash
cd testing
jupyter nbconvert --to notebook --execute --inplace blackbox_tests.ipynb
jupyter nbconvert --to notebook --execute --inplace whitebox_tests.ipynb
```

Each notebook ends with an `assert` that fails if any test fails, so a notebook that
runs to the end without error means all tests passed.

- `blackbox_tests.ipynb`: equivalence partitioning, boundary value analysis,
  cross-base consistency (requirements RF-01 to RF-17).
- `whitebox_tests.ipynb`: statement, branch, loop and path coverage over `func`,
  plus a `trace`-based coverage measurement.
