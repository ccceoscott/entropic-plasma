---
name: json-to-pydantic
description: JSON-to-Pydantic model converter — generates type-safe Pydantic v2 models from raw JSON payloads for Python Cloud Functions and AI agents.
phase: "209"
category: backend
tags: ["pydantic", "python", "json", "type-safety", "models"]
---

# Json To Pydantic (R.A.P.S.) — Phase 207.16

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
