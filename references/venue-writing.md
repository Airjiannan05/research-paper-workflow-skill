# Venue-Aware Writing

Use venue awareness to shape paper structure, not to assert final compliance. Current page limits, anonymity rules, checklists, and artifact policies can change; use web search before final submission advice.

## Default venue families

| Venue family | Writing emphasis | Common risk |
|---|---|---|
| AAAI/IJCAI | clear AI problem, generality, rigorous experiments, readable motivation | contribution looks incremental or too domain-specific |
| NeurIPS/ICLR/ICML | conceptual novelty, strong empirical/proof evidence, ablations, limitations | weak baselines, insufficient insight, unclear mechanism |
| CVPR/ICCV/ECCV | benchmark strength, visual evidence, dataset protocol, qualitative analysis | missing comparisons or unfair setup |
| ACL/EMNLP/NAACL | task framing, datasets, evaluation validity, linguistic/LLM analysis | benchmark contamination or shallow error analysis |
| SIGIR/KDD/WWW | system/data setting, practical metrics, scalability, user/platform relevance | weak real-world validity |
| GECCO/PPSN | evolutionary computation mechanism, search-space design, statistical testing | only applying GP/EA to a new domain |
| Systems venues | design constraints, implementation, measurement, ablation, workload realism | toy setting, poor reproducibility |

## Section budget heuristic

For a full draft without verified venue rules:

- Abstract: 150-250 words.
- Introduction: 12-18%.
- Background/related work: 15-20%.
- Method/system: 25-30%.
- Experiments: 25-35%.
- Limitations/ethics/reproducibility/conclusion: 5-10%.

If the draft is too short, expand with mechanism detail, exact claim-to-test mapping, experiment protocol, ablation rationale, error analysis, and limitation boundaries. Do not inflate with generic motivation.

## Venue-aware output block

For manuscript-level outputs, include a compact status block after the draft:

```text
Venue assumption:
Length status:
Evidence placeholders:
Citation placeholders:
Fresh-rule check needed:
Next mode:
```
