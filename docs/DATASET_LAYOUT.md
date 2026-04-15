# Dataset Layout Notes

This file should explain how the public dataset release is organized and how the code repository expects to read it.

## Expected task bundle

Each problem bundle should contain:

- `problem.md`
- `config.yaml`
- `testbench.v`

The default public release excludes `reference.v`.

## Expected directory structure

```text
data/
├── L1_basic/
├── L2_sequential/
├── L3_module/
├── L4_system/
└── L5_ultimate/
```

If the final public release uses different names or merges tiers, update this file to match the exported snapshot exactly.

## Public-release default

Public evaluation only needs the task brief, interface metadata, and testbench. Reference RTL remains a benchmark-side validation anchor and is excluded from the default public dataset release.
