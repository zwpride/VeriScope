# VeriScope

Open benchmark and evaluation suite for first-pass Verilog coding.

This repository is the public code release for `VeriScope`.

## What this repository contains

- benchmark-side evaluation code
- benchmark bundle validators
- execution harness integration
- judge prompts and scoring rules
- scripts for reproducing the main reported comparisons
- documentation for the released benchmark package

## Suggested repository layout

```text
veriscope/
├── README.md
├── LICENSE
├── requirements.txt
├── REPRODUCIBILITY.md
├── docs/
│   ├── DATASET_LAYOUT.md
│   ├── THIRD_PARTY_ASSETS.md
│   └── SAFETY_AND_LIMITATIONS.md
├── evaluator/
├── judge/
├── scripts/
├── tools/
├── prompts/
├── examples/
└── results/
```

## Scope

VeriScope evaluates first-pass Verilog generation in a deployment-style workflow. Each task is packaged as a reusable problem bundle, and each model run is scored with:

- objective execution
- RTL-level review
- artifact-level review

The public paper reports results on 568 benchmark problems, with analysis over both the full benchmark and the stricter `L3--L4+` slice.

The companion Hugging Face dataset release excludes `reference.v` by default. Public evaluation only needs the task brief, interface metadata, and testbench. Reference RTL is treated as a benchmark-side validation anchor rather than as part of the default public evaluation package.

- code repository: `https://github.com/zwpride/VeriScope`
- dataset repository: `https://huggingface.co/datasets/zwpride/VeriScope`

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 scripts/run_public_eval.py \
  --problems data/public_subset \
  --predictions examples/sample_predictions.json \
  --output outputs/sample_eval.json
```

## Reproducibility

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for:

- exact environment setup
- required external tools
- minimal reproduction commands
- which results are fully reproducible from the public release
- which evaluations depend on third-party closed APIs

## Dataset release

The benchmark bundles live in a companion Hugging Face dataset repository. This code release should link to that dataset and pin the expected dataset version or tag. The default public dataset is expected to contain:

- `problem.md`
- `config.yaml`
- `testbench.v`

and to exclude `reference.v` unless a separate maintainer-oriented validation package is released.

## Release checklist

- replace the draft public entrypoint names with the final scripts
- update the repository tree to match the final exported layout
- add a pinned release tag that matches the published release snapshot
