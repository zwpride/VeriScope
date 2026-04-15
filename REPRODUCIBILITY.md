# Reproducibility Notes

This file is the public reproduction guide for the GitHub release.

## Environment

- Python: `3.12.12`
- Icarus Verilog: `12.0`
- Yosys: `0.33`
- Verilator: `5.020`
- OS: `Ubuntu 24.04.2 LTS`

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Public reproduction paths

### 1. Minimal smoke test

```bash
python3 scripts/run_public_eval.py \
  --problems data/public_subset \
  --predictions examples/sample_predictions.json \
  --output outputs/smoke_test.json
```

### 2. Objective execution only

```bash
python3 scripts/run_public_eval.py \
  --problems data/release_snapshot \
  --predictions examples/sample_predictions.json \
  --mode functional \
  --output outputs/functional_eval.json
```

### 3. Full quality-aware evaluation

```bash
python3 scripts/run_public_eval.py \
  --problems data/release_snapshot \
  --predictions examples/sample_predictions.json \
  --mode full \
  --output outputs/full_eval.json
```

## Closed-model dependencies

Some leaderboard results in the paper depend on third-party model APIs that are not redistributed here. The public release should make this explicit.

- Fully reproducible from the public release:
  - benchmark bundle loading
  - compilation and simulation
  - Yosys synthesis checks
  - Verilator lint checks
  - score aggregation over provided predictions
  - public bundle validation without access to `reference.v`

- Not fully reproducible without external API access:
  - proprietary model generations
  - proprietary judge calls, if still used in the public pipeline

## What to pin before release

- git commit or tag
- dataset version
- prompt version
- judge config version
- release date
