# Review Methodology

## Review Type

Working classification: structured critical review with systematic mapping elements.

The review should be broad and analytical enough for Artificial Intelligence Review while still documenting search logic, inclusion criteria, screening decisions, citation-verification status, and synthesis methods. The assembled manuscript methodology is in `12_manuscript/main_manuscript.md`; the section-level source draft remains `07_draft_sections/02_review_methodology_search_protocol.md`.

## Databases Searched

- Google Scholar.
- Semantic Scholar.
- IEEE Xplore.
- ACM Digital Library.
- ACL Anthology.
- ISCA Archive.
- SpringerLink.
- ScienceDirect.
- arXiv.
- Papers With Code.

## Search Period

Search activity is recorded in `02_literature_search/search_log.csv`. Current repository records support logged search and verification activity, but they do not support a complete PRISMA-style global retrieval window or total retrieval count.

## Inclusion Criteria

Use `01_scope_and_planning/inclusion_exclusion_criteria.md` as the current source of inclusion criteria.

## Exclusion Criteria

Use `01_scope_and_planning/inclusion_exclusion_criteria.md` as the current source of exclusion criteria.

## Screening Procedure

1. Run database searches using documented queries.
2. Record each search in `02_literature_search/search_log.csv`.
3. Screen titles and abstracts for relevance.
4. Record decisions in `02_literature_search/screening_log.csv`.
5. Track rejected but possibly useful papers in `02_literature_search/rejected_papers_log.csv`.
6. Create structured notes for included papers.

## Synthesis Method

- Group papers by method family and challenge type.
- Fill synthesis matrices before drafting claims.
- Use `05_synthesis_matrices/evidence_to_claim_matrix.csv` to connect major claims to supporting evidence.
- The canonical claim-tracking file is `05_synthesis_matrices/evidence_to_claim_matrix.csv`. The older `claims_evidence_map.csv` has been archived and should not be updated.
- Convert matrices into thematic prose, not paper-by-paper listing.

## Limitations Of Review Process

The review is evidence-controlled but not a fully exhaustive systematic review. Limitations include incomplete global retrieval counts, broad discovery rows in the search log, uneven database and language coverage, variable metadata quality, and conservative handling of preprint or watchlist evidence. Pashto may be used only as a selective illustrative example, not as a focused case-study contribution.
