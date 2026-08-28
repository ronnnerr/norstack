---
name: headed
description: Open a visible Chromium window you can watch. Use for CAPTCHA, login, OAuth, or when you want to see the browser. Uses the norstack browse binary.
---

# headed

```bash
B="$HOME/norstack/bin/browse"
$B connect                          # visible window + extension
$B handoff "Need you on this login"
# wait for the operator
$B resume
$B disconnect                       # back to headless
```

Use this instead of any gstack `open-gstack-browser` / connect-chrome skill. Same engine, norstack voice.

Three failed headless interactions → handoff. Don't loop.
