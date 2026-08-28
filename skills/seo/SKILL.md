---
name: seo
description: Technical and on-page SEO audit. Use for the agency sites, client landings, the video product marketing, "why isn't this ranking," crawl/index/meta/CWV. Browse the live page. Don't curl and guess.
---

# seo

Default to the current project until you name another site. Load `profile`.

## How you look

Use `browse`. `web_fetch` / curl miss JS-injected JSON-LD. For schema:

```bash
B="$HOME/norstack/bin/browse"
$B goto URL
$B js "JSON.stringify([...document.querySelectorAll('script[type=\\'application/ld+json\\']')].map(s=>s.textContent))"
$B data --jsonld --og --meta
```

Also: robots.txt, sitemap.xml, title, H1, canonical, console errors, screenshot.

## Order

1. **Can it be crawled and indexed?** robots, sitemap, noindex, canonicals, HTTPS, redirect loops
2. **Is it fast and usable?** LCP / INP / CLS, mobile, `responsive`
3. **On-page** unique title 50–60, one H1, intent match, internal links, image alt
4. **Does it deserve to rank?** thin pages, duplicates, no proof
5. **Authority** only after 1–4

## Report

Top 5 issues. Each: what's wrong, impact, evidence (URL + what you saw), fix, priority.

No "consider improving." Name the file or tag.

## Operator overlays

- Client pages: their brand keywords, not the desktop app language.
- Don't invent Search Console numbers you didn't see.
- After you change meta/canonical, `browse` the page again.
- Schema false-negative from curl is a miss. Use browse.
