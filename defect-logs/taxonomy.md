# Defect Taxonomy

Severity scale: **Critical** (unsafe/unimplementable), **High** (likely wrong system), **Medium** (rework), **Low** (cosmetic).

| # | Category | Definition | Example (PSVS) |
|---|---|---|---|
| 1 | Ambiguity | A statement admits more than one valid interpretation. | S1: 'registered depositors' - registered by whom, and how? |
| 2 | Vagueness | A term or quantity is imprecise, with no threshold or boundary. | S2: 'a large number of boxes'; S9: 'promptly'. |
| 3 | Incompleteness | Needed information, cases, actors or exception handling are missing. | S8: nothing says what happens to boxes inside a chamber being warmed. |
| 4 | Contradiction | Two statements cannot both be satisfied at once. | S7 'never above -18C' vs S8 'warmed to 0C'. |
| 5 | Non-verifiability | No finite, objective test or measurement can show the requirement is met. | S12: 'a good audit trail'; S6: 'safe temperature'. |
| 6 | Redundancy | The same constraint is stated more than once, risking drift. | S6 (safe temperature) restates S7 in general form. |
| 7 | Infeasibility | Cannot be achieved with known physical, technical or legal means. | S9: flagging low viability promptly needs viability measurement, which is destructive and slow. |
| 8 | Untraceability | A requirement or scenario statement has no source, ID, or link to a counterpart. | Scenario says 'one species per box'; no S-requirement captures it, yet S10 depends on it. |
| 9 | Inconsistency (terminology/units) | The same concept is named or measured differently across statements. | Scenario: 'several chambers'; S3 fixes exactly four. |
| 10 | Unstated assumption | The requirement silently depends on a fact or condition never recorded. | S10 assumes a defined 'year' and a baseline box count. |
