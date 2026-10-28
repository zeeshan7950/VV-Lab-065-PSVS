# VV-Lab-065-PSVS: Polar Seed Vault Specification - Verification & Validation Lab

Requirements inspection of the Polar Seed Vault System (PSVS): a vault holding sealed boxes of crop seeds
deposited by registered institutions. The vault is a custodian; depositors keep ownership.

## Repository layout
| Folder | Purpose |
|---|---|
| `/requirements` | Baselined requirements (S1-S12) and change-request template |
| `/defect-logs` | Defect taxonomy, defect log, peer-review comparison, chart, helper scripts |
| `/abstractions` | Abstraction of the domain (later labs) |
| `/models` | Formal models (later labs) |
| `/operations` | Operation specifications (later labs) |
| `/constraints` | Invariants and constraints (later labs) |
| `/proofs` | Proof obligations and proofs (later labs) |
| `/reports` | Lab reports and summaries |

## Configuration management
- `main` holds reviewed work only; analysis is done on feature branches (e.g. `defect-analysis`) and merged with `--no-ff`.
- Baseline: tag `baseline-1` = commit `PSVS-REQ-v1.0` (S1-S12 as issued).
- Any change to a baselined artifact needs a change request (`requirements/change-request-template.md`).

## Reproducing the reports
`python3 defect-logs/tools/generate_reports.py` rebuilds the summary table and chart from `defect_log.csv`.
`python3 defect-logs/tools/peer_compare.py <mine> <peer> <common>` computes detection rates.
