**Shipped: Benford GL QuickCheck (Python)**

I built a tiny audit-analytics tool that runs a first-digit Benford test on any General Ledger CSV and spits out a chart + short report in seconds.

- Single file (`benford_gl_quickcheck.py`), no external services
- Uses pandas + matplotlib
- Outputs: `benford_chart.png` and `REPORT.md` (rows evaluated, MAD vs. Benford, most over/underrepresented digits)

Why this matters: Benford analysis is a common screening test in audit/forensics to spot unusual number patterns in journal entries. It’s not a smoking gun, but it’s a fast way to focus follow-up work.

If you want the repo/template or a version that runs in the browser, DM me and I’ll share.
