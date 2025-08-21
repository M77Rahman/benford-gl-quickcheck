#!/usr/bin/env python3
"""Benford GL QuickCheck
Usage:
  python benford_gl_quickcheck.py --csv sample_gl.csv --column amount
Outputs:
  - benford_chart.png
  - REPORT.md
"""
import argparse, math
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def expected_benford():
    return {d: math.log10(1 + 1/d) for d in range(1,10)}

def first_digit_freq(series):
    s = pd.Series(series).astype(float).abs()
    s = s[s > 0]
    first_digits = s.astype(str).str.replace(".", "", regex=False).str.lstrip("0").str[0]
    first_digits = pd.to_numeric(first_digits, errors="coerce").dropna().astype(int)
    counts = first_digits.value_counts().sort_index()
    total = counts.sum()
    freq = (counts / total).reindex(range(1,10), fill_value=0.0)
    return freq, counts, int(total)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to GL CSV")
    ap.add_argument("--column", default="amount", help="Numeric amount column name (default: amount)")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    if args.column not in df.columns:
        raise SystemExit(f"Column '{args.column}' not found. Available: {list(df.columns)}")

    freq, counts, total = first_digit_freq(df[args.column])
    exp = pd.Series(expected_benford())
    diff = (freq - exp).abs()
    mad = float(diff.mean())

    # Chart (single plot, no explicit colors)
    plt.figure(figsize=(7,4))
    plt.title("Benford First-Digit Analysis")
    plt.plot(exp.index, exp.values, marker="o", label="Expected (Benford)")
    plt.plot(freq.index, freq.values, marker="o", label="Observed")
    plt.xlabel("Leading Digit")
    plt.ylabel("Frequency")
    plt.xticks(range(1,9+1))
    plt.legend()
    plt.tight_layout()
    plt.savefig("benford_chart.png", dpi=160)
    plt.close()

    report = f"""# Benford GL QuickCheck — Report

- Rows evaluated: **{total}**
- Mean absolute deviation (MAD) vs Benford: **{mad:.6f}**
- Most overrepresented digit: **{(freq - exp).sort_values(ascending=False).index[0]}**
- Most underrepresented digit: **{(exp - freq).sort_values(ascending=False).index[0]}**
- Run at: **{datetime.utcnow().isoformat()}Z**

See `benford_chart.png` for the curve comparison.

> Note: Benford analysis is a screening test. Investigate context, data generation, and business rationale before concluding anything.
"""
    with open("REPORT.md", "w") as f:
        f.write(report)

if __name__ == "__main__":
    main()
