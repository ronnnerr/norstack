---
name: secure
description: Security audit. Use when hunting secrets, reviewing auth, threat modeling, checking skill supply chain, or hardening an app before it goes public. Read-only, reports like a defender, never writes exploits.
---

# secure

your security audit. Built on OWASP Top 10 and OWASP Agentic Skills Top 10 (AST10). Reports like a defender. Does not write exploits.

Default is **daily**: only findings you could explain to the user in one sentence with a file:line. Comprehensive is opt-in when you say deep / monthly.

## Scope for this operator

Prioritize what you actually run:

1. Secrets in git and `.env` (an exchange API keys, wallet seeds, API tokens)
2. Skill supply chain (`~/norstack/skills`, `~/.grok/skills`, downloaded marketplaces)
3. LLM tool use: user text into shell, unvalidated tool args
4. App auth / RLS in any app you ship
5. Local-first apps: nothing personal uploaded "to be helpful"
6. Then classic OWASP on the repo in cwd

## Run

1. Detect stack from lockfiles. Read README. Map attack surface. No findings yet.
2. **Secrets HOW.** `git ls-files '*.env' '.env.*'` minus examples. `git log -p --all -G 'AKIA|sk-ant-|sk_live_|ghp_|xoxb-|BEGIN .* PRIVATE KEY|mnemonic|seed phrase'`. Tracked `.env` not gitignored = HIGH. Quote the line. Never probe a live API.
3. **Leak surfaces beyond git:** `~/.norstack/`, session transcripts, Telegram bots, vault files, browser cookie dumps, `~/Media/norstack/drop`. List paths, do not dump contents into chat.
4. **Key material.** Inventory only: what kind of credential, where it lives, whether it is tracked. Never print a secret. Never sign, send, or export anything. A finding is "key material sits in a tracked file," never a how-to.
5. Deps: lockfile present and tracked. Audit tool if it exists. Note skips.
6. CI: unpinned actions, `pull_request_target`, secrets in `run:`.
7. LLM / agent: user text into shell, `eval` of model output, skills that curl + env.
8. **Skills inventory.** First-party = `~/norstack/skills`. Marketplace = everything else under `~/.grok/skills` and `~/.claude/skills` that is not a norstack symlink. Hash SKILL.md vs last report in `~/.norstack/security/` if one exists. Review scripts/hooks for network + env. norstack is trusted unless it grew a curl-to-env.
9. OWASP A01–A10 only where that surface exists.
10. Filter. Daily bar: 8/10 + a quoted line. No exploit PoC.

## If you find a live secret

1. Tell the user. Do not paste the full secret again.
2. Wallets: **move funds first**, then rotate.
3. Revoke the key at the provider. Rotate. Scrub history (`git filter-repo` / BFG) only if you asked.
4. Never probe whether the key still works.

## Finding shape

```
[SEV] (n/10) file:line — one sentence
Exploit path: 3 steps, no payload
Fix: the change
```


## Hard rules

- Read-only. Recommend. Do not patch unless you said fix.
- Never test a stolen key against a live API.
- Never write malware, exploits, or attack a system.
- Disclaimer at the end: first pass, not a hired pentest.

## Do not

- Scan the whole home directory unless you asked.
- Flag localhost docker-compose root as CRITICAL.
