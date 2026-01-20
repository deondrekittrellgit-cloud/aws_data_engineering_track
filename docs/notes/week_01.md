# Week 1 — Environment + Local Postgres

## Completed
- Repo created and pushed to GitHub
- .env ignored via .gitignore
- Colima running with QEMU (MacPorts QEMU)
- Postgres running via docker compose
- Host port: 5433 -> container port: 5432
- Init scripts:
  - sql/postgres/01_schema.sql
  - sql/postgres/02_seed.sql
- Verified:
  - psql connection via DE_DB_URL
  - tables exist + seed data loaded
  - DBeaver test connection passed
