---
name: postgres
description: Postgres and Supabase. Use when writing SQL, migrations, row level security, or indexes, and when diagnosing a slow query.
---

# postgres

Use this for Postgres and Supabase. A local SQLite app is a different problem, do not apply this file to it.

## Critical

**Queries**
- Index what you filter and join on. If `EXPLAIN` says Seq Scan on a hot path, fix it.
- Select the columns you need. No `select *` in app queries.
- Pagination with a stable key (`id` / `(created_at, id)`), not giant `OFFSET`.
- Don't wrap indexed columns in functions (`where lower(email) =` without an expression index).

**Connections**
- App traffic through the pooler. Don't open a new client per request.
- Serverless: transaction mode. Session features (prepared statements, advisory locks) need session mode or a sticky connection.
- Time out idle transactions. They hold locks and eat the pool.

**Security / RLS**
- RLS on every table that a client can touch. Default deny.
- Policies must be indexed or they become seq scans per row.
- Test as two users. "It works in the SQL editor as postgres" is not a test.
- Service role bypasses RLS. Never expose it to the browser.

## High

**Schema**
- `uuid` or `bigint` PKs. Don't use sequential ints if the client can see them and enumerate.
- `timestamptz`, not `timestamp`.
- `text` + check, not `varchar(255)` theater.
- Foreign keys. Soft deletes need an index on `(deleted_at)` or a partial `where deleted_at is null`.

**Locks**
- Short transactions. No HTTP inside a transaction.
- Add columns as nullable first. Backfill. Then constrain.
- `create index concurrently` on live tables.

## Operator overlays

- One product's data does not belong in another product's database. Project isolation is a schema decision.
- Migrations live in the repo and run in CI. Don't "just fix prod."
- After a policy change, prove it with two roles. Then `verify`.

## Don't

- Enable Realtime on a table to debug. You'll leak rows.
- Store secrets in Postgres. That's what the vault / env is for.
- Invent RLS that "should" work. Run it.
