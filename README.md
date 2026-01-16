# AWS Data Engineer Track — 24-Week Workspace

This repo is my end-to-end Data Engineering workspace for building:
- Reliable Python pipelines (ingest -> transform -> validate)
- Postgres modeling + tests
- AWS S3/Athena lake patterns (raw/clean/curated + partitions)
- Orchestration (Airflow) + transformations (dbt)
- CI (GitHub Actions), runbooks, and architecture docs

## Quickstart (local)
```bash
make venv
make install
make test
```

## Repo structure
- `src/` — Python package (production-style layout)
- `tests/` — unit + integration tests (pytest)
- `scripts/` — helper scripts (CLI tasks)
- `sql/` — Postgres + Athena query packs
- `docs/` — design docs, runbooks, diagrams
- `data/` — small sample inputs only (avoid committing large raw data)

## Notes
- Never commit `.env` (use `.env.example`)
