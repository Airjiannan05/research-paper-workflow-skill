# Source Verification Protocol

Use this file whenever a task depends on externally queried information: literature search, recent competitor monitoring, venue rules, benchmark/dataset status, tool/library/version claims, pricing/compute availability, citation metadata, citation-context support, biographical/current-role facts, and any claim the user asks to verify.

## Non-negotiable rule

For every externally queried factual item, verify it three times before treating it as usable evidence. If three checks are not possible, label the item `unverified` or `partially verified` and do not use it as a load-bearing claim.

## Triple-check protocol

For each important source-backed fact, run these checks:

1. **Existence check**: confirm that the source, paper, venue rule, dataset, repository, or artifact exists at a primary or highly reliable source.
2. **Metadata check**: confirm title/name, authors/owners, date/version, venue/source, URL/DOI/arXiv ID/repository path, and whether it is current or superseded.
3. **Support check**: confirm that the cited passage or retrieved evidence actually supports the claim being made. Do not cite a source only because it is topically related.

Prefer three independent anchors when available:

- primary source: paper PDF, official proceedings, arXiv/OpenReview, official venue page, official docs, official repository, dataset card;
- index or cross-check source: Semantic Scholar, Crossref, DBLP, Papers with Code, official benchmark leaderboard, package registry;
- internal consistency check: source text passage, abstract/method/result table, README release notes, or another independent source.

## Reliability tiers

Use sources in this order when possible:

1. Official paper/proceedings/preprint PDF, official venue documentation, official repository/docs, official dataset/benchmark page.
2. Recognized scholarly indices or infrastructure: Semantic Scholar, Crossref, DBLP, OpenReview, Papers with Code, package registries.
3. Reputable technical reports, lab pages, institutional pages, or maintainer discussions.
4. Blogs, social posts, secondary summaries, and search snippets only as discovery leads, not final evidence.

## Source verification log

For non-trivial search outputs, include or update a compact `source_verification_log` table:

| claim_or_fact | source_1_existence | source_2_metadata | source_3_support | verdict | notes |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | verified / partial / unverified / conflict | TBD |

Keep the table concise in normal responses. For large projects, store it as `source_verification_log.md` using `assets/source_verification_log_template.md`.

## Claim wording rules

- `verified`: may be used as a normal claim with citation/source reference.
- `partial`: may be used with cautious wording such as "appears", "reported by", or "according to".
- `unverified`: may only be listed as a lead or TODO, not as evidence.
- `conflict`: state the conflict, cite both sides if possible, and do not resolve it by guessing.

## Citation-context audit

When auditing citations inside a manuscript, check:

- citation exists and metadata matches;
- citation is the right work, not a similarly titled work;
- the cited section supports the sentence;
- the sentence does not overgeneralize beyond the source;
- numeric values, dataset names, benchmark scores, dates, and claims match the source;
- the reference is not retracted, superseded, or outdated for the purpose being claimed.

## Current-information triggers

Always use current web search for:

- venue rules, deadlines, page limits, checklist requirements, AI disclosure, anonymity, supplementary material rules;
- latest papers, arXiv/OpenReview status, code release status, benchmark leaderboards;
- software/library APIs, tool availability, hardware/pricing, package versions;
- legal, ethical, privacy, IRB, copyright, or dataset license questions.

## Failure behavior

If verification fails, do not fill the gap with plausible text. Instead output:

- what could not be verified;
- which checks passed or failed;
- what source would be needed;
- a safe placeholder such as `[VERIFY]`, `[CITE NEEDED]`, `[RESULT NEEDED]`, or `[RULE CHECK NEEDED]`.
