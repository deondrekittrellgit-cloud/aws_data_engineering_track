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

## Local Postgres (Docker + Colima)

### Prereqs
- Colima running (Docker context set to `colima`)
- Docker Compose available

Quick check:
```bash
docker context use colima
docker info
```

### Start Postgres
From the repo root:

```bash
docker compose up -d
docker compose ps
```


### Connect with psql (from your Mac)
Example (your port is **5433**):

```bash
export DE_DB_URL="postgresql://de_user:de_password@localhost:5433/de_db"
psql -P pager=off "$DE_DB_URL" -c "SELECT version();"
psql -P pager=off "$DE_DB_URL" -c "\dt"
```

### Reset the database (re-run init scripts)
This wipes the Docker volume and re-runs `sql/postgres/*.sql`:

```bash
docker compose down -v
docker compose up -d
```


### Troubleshooting
If Docker commands fail, make sure Colima is running:

```bash
colima start --vm-type qemu --cpu 2 --memory 4 --disk 40
docker context use colima
docker info
```

If Postgres isn’t reachable from your Mac:

```bash
docker compose ps
lsof -nP -iTCP:5433 -sTCP:LISTEN
```
