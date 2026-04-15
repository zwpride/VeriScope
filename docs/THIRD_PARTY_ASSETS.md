# Third-Party Assets and Licenses

This release separates public benchmark bundles from third-party source material used during benchmark construction.

## Summary

| Asset | Role | URL | License / terms | Redistribution status | Notes |
|---|---|---|---|---|---|
| HDLBits source material | source crawl used during benchmark construction | https://hdlbits.01xz.net | no clear machine-readable public license found in the source pages used for curation | not redistributed verbatim | public task briefs are rewritten benchmark bundles rather than raw HDLBits statements |
| Icarus Verilog | compilation and simulation backend | https://steveicarus.github.io/iverilog/ | GPL-2.0-or-later | dependency only | required for public execution-based evaluation |
| Yosys | synthesis checks and circuit artifacts | https://github.com/YosysHQ/yosys | ISC | dependency only | used for objective backend checks and structural artifacts |
| Verilator | lint checks | https://verilator.org | LGPL-3.0-or-later or Artistic-2.0 | dependency only | used for objective backend lint validation |

## Release policy

- Raw third-party source prompts are not redistributed as part of the default public dataset.
- Public benchmark bundles are released as newly authored task packages with benchmark-side metadata and testbenches.
- External tools are required runtime dependencies rather than redistributed binaries.
