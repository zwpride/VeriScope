# Safety and Limitations

## Intended use

VeriScope is intended for evaluation of first-pass Verilog generation systems.

## Not intended for

- certification of production RTL
- security review of generated hardware logic
- sign-off for synthesis, timing closure, or tapeout

## Known limitations

- one-shot evaluation setting
- incomplete decontamination for public third-party models
- limited top-end expert-scale coverage
- judge-based quality components may still require periodic recalibration
- the default public release excludes `reference.v`, so benchmark-side gold validation is not fully reproduced from the dataset alone

## Potential misuse

Improved first-pass Verilog generation can accelerate legitimate hardware development, but it can also lower the barrier to producing unsafe, unauthorized, or malicious RTL. Public release documentation should state this clearly.
