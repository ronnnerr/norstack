---
name: react
description: Next.js and React performance for your apps. Use when writing or reviewing the video product, pred, the journal app, or any React/Next code — waterfalls, bundles, RSC, re-renders.
---

# react

the video product, pred, and the journal app are Next apps. the desktop app webview is React. This is the law for those codebases.

Load `profile` first. Don't carry one project's chrome onto another.

## Do these, in this order

**1. Waterfalls (kill first)**
- Cheap sync checks before any `await`
- Independent work in `Promise.all`
- Start fetches early, await late
- Don't await a flag you could have branched on first

**2. Bundle**
- No barrel imports (`import { x } from '@/components'` that re-exports the world)
- `next/dynamic` for heavy UI (charts, editors, video players)
- Analytics and chat widgets after hydration
- Import paths must be statically analyzable

**3. Server**
- Auth every server action like an API route
- `React.cache()` for per-request dedup
- Don't ship fat objects to client components
- No module-level mutable request state
- `after()` for non-blocking side work

**4. Client fetch**
- Dedup. Don't fire the same GET from three components
- Version anything you write to localStorage

**5. Re-renders**
- Derive during render. Don't `useEffect` to set state from props
- No components defined inside components
- Primitive effect deps. Functional `setState`
- `startTransition` for non-urgent UI

**6. Render**
- Ternary, not `&&`, for possible `0` / empty string
- Hoist static JSX
- Don't animate SVG roots

## Operator overlays

- After a user-visible UI change, `browse` it. React that "looks right in code" is not done.
- the desktop app: keyboard path first. No spinner where an optimistic update will do.
- pred: never invent a number to make a component happy. Read disk or API.
- the video product: video players and editors are the heavy bits. Dynamic-import them.

## Don't

- Memo everything. Memo expensive work only.
- Add SWR because a blog said so if the repo already has a fetcher.
- Touch SQLite/the desktop app local DB rules here. That's not this skill.
