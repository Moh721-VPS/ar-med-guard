# Labeling Guide

## Labels
| Label | Meaning |
|---|---|
| `misleading` | Presents a stem cell treatment as proven, safe, or curative without approved clinical evidence |
| `not_misleading` | Accurate, hedged, or evidence-based statement (e.g. approved uses such as bone marrow/blood stem cell transplants, or warnings about unproven clinics) |
| `unclear` | Cannot decide. Excluded from training |

## Mark as `misleading` if the claim:
- Promises a cure or guaranteed results (e.g. autism, diabetes, paralysis, MS, aging)
- Says the treatment has "no side effects" or is "100% safe"
- Uses testimonials as proof of effectiveness
- Cites no trials, regulators, or credible sources while claiming medical benefit
- Sells an unapproved treatment with urgency or high-pressure marketing

## Mark as `not_misleading` if the claim:
- Describes approved, evidence-based stem cell use accurately
- Warns about unproven therapies or clinics
- Reports research honestly, including its limits

## Rules
- Label the text, not whether you like the source.
- Keep dialect and spelling as written. Do not clean or correct the Arabic.
- Aim for a balanced dataset (roughly 50/50).
- Every claim needs `source_url` and `date`.
- Two people should label the same 30 claims to check agreement.

## Columns
`id, text, label, source_type, dialect, source_url, date, labeler`

- `source_type`: ad / post / testimonial / news / other
- `dialect`: MSA / Gulf / Egyptian / Levantine / Maghrebi / mixed / unknown

## Reference
ISSCR patient guidance on stem cell clinics (isscr.org).
