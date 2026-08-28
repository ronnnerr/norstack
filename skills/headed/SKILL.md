---
name: headed
description: Open a visible Chromium window you can watch. Use for CAPTCHA, login, OAuth, or any flow the headless browser cannot finish on its own.
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


Three failed headless interactions → handoff. Don't loop.
