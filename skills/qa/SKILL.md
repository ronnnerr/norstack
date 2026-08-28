---
name: qa
description: QA a site or local app in a real browser. Use when asked whether something works, to walk a flow end to end, or to find bugs on a URL.
---

# qa

Use `browse`. Do not use Playwright MCP or a second Chromium.

## Loop

1. Detect the project (`profile`) and the URL (local first).
2. `$B goto` the URL. If it won't load, that's the first bug.
3. `console --errors` and `network`. JS errors are bugs.
4. Walk the critical path you care about. Snapshot, click, fill, screenshot.
5. `responsive` if it's a site humans see on phones (landings, apps, client sites). Skip for internal tools unless asked.
6. Read every screenshot.
7. File bugs as a tight list: severity, where, what you saw, repro. Fix if the operator asked to fix. Otherwise report.

## Desktop apps

If it's the Tauri app, still browse any webview URL you can reach, and say what you could not reach from headless.

## Done

A QA pass without screenshots is not a QA pass.
