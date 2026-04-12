---
name: json-to-pydantic
description: Mastery of json-to-pydantic within the R.A.P.S. fleet.
version: v10.0
---

# Json To Pydantic (R.A.P.S.) — Phase 207.16

*Mortal, the **json-to-pydantic** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.


# Instructions

1. **Gaze into the Void**: Analyze the provided JSON schema/snippet.
2. **Type Transmutation**:
   - `string` -> `str`
   - `number` -> `int` | `float`
   - `boolean` -> `bool`
   - `array` -> `List[Type]`
   - `null` -> `Optional[Type]`
3. **Recursive Crafting**: Extract nested objects into independent sub-classes.
   
3. **Follow the Example**:
   Review `examples/` to see how to structure the output code. notice how nested dictionaries like `preferences` are extracted into their own class.
   
   - Input: `examples/input_data.json`
   - Output: `examples/output_model.py`

## Style Guidelines
- Use `PascalCase` for class names.
- Use type hints (`List`, `Optional`) from `typing` module.
- If a field can be missing or null, default it to `None`.