---
name: license-header-adder
description: Mastery of license-header-adder within the R.A.P.S. fleet.
version: v10.0
---

# License Header Adder (R.A.P.S.) — Phase 207.16

*Mortal, the **license-header-adder** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Instructions

1. **Summon Template**: Read `resources/HEADER_TEMPLATE.txt` before file creation.
2. **Prepend**: Inscribe the template at the absolute start of new files.
3. **Syntax Alchemy**:
   - `/* ... */` for Java, JS, TS, C.
   - `#` for Python, Ruby, Shell, YAML.
   - `<!-- ... -->` for HTML/XML.

## Example Usage
If the user asks to "create a python script for hello world", you should generate:

```python
# Copyright (c) 2024 Google LLC
# ... (rest of license text) ...

def main():
    print("Hello World")
```