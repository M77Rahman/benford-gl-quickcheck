# Benford GL QuickCheck

A fast, single-file **Benford's Law** first-digit check for general ledger data.

## Why it matters
Benford analysis is widely used in audit/forensics as a *screening* test to spot unusual number patterns in journal entries and transactions.

## Features
- Reads any CSV with a numeric amount column (default: `amount`)
- Outputs a chart (`benford_chart.png`) and a short `REPORT.md`
- Zero external services. Python + pandas + matplotlib only.

## Quickstart
```bash
pip install pandas matplotlib
python benford_gl_quickcheck.py --csv sample_gl.csv --column amount
```

## Input format
CSV with at least one numeric column, e.g.:
```csv
date,user,account,amount,memo
2024-01-01 00:00:00,FIN_AP,2000-AP,-123.45,Invoice
...
```

## Notes
- Treat results as *indicators* for deeper work, not conclusions.
- Zeros and signs are handled (we take absolute value and ignore zeros).
- Works on any numeric scale (we analyze leading digits).

## License
MIT
