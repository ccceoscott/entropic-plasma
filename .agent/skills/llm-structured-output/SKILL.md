---
name: llm-structured-output
description: Mastery of llm-structured-output within the R.A.P.S. fleet.
version: v10.0
---

# LLM Structured Output (R.A.P.S.) — Phase 207.16

*Mortal, the **llm-structured-output** is a shard of the infinite. Bound by the Decree of Zoltan, it serves the Infinity Protocol. Use it with reverence.*

> [!CAUTION]
> **Sovereign Execution**: Prepend Node 22 path. `NODE_OPTIONS=--max-old-space-size=4096`.

## Structural Mandate
- **Zod Inscription**: Define all targets via `zod-backend-dmz`.
- **Native Primacy**: Prioritize provider-native schema enforcement (Strict Mode).
- **Validation Wards**: All LLM outputs MUST be parsed and validated before use.
- **Retry Logic**: Implement recursive correction (max 3) for validation failures.

## Provider Matrix
| Provider | Implementation | Key Config |
|---|---|---|
| **OpenAI** | `response_format: { type: "json_schema" }` | `"strict": true`, `additionalProperties: false`. |
| **Anthropic** | `tool_choice: { type: "tool", name: "x" }` | Force tool usage for structured extraction. |
| **Google** | `generationConfig.responseSchema` | Set `responseMimeType: "application/json"`. |

## Validation & Extraction
```typescript
const Schema = z.object({ result: z.string().describe("Detail...") });
// OpenAI (Helper)
const completion = await client.beta.chat.completions.parse({
  model: "gpt-4o-2024-08-06",
  response_format: zodResponseFormat(Schema, "extraction")
});
```

## Anti-Patterns (NEVER DO)
- Parse raw text blocks for data when tool-calling is active.
- Use `json_object` mode without a defined schema.
- Omit `description` strings for schema fields (the model needs them for context).
- Assume "Valid JSON" == "Correct Data". Perform semantic validation.

## Edge Case Handling
- **Refusals**: Check `message.refusal` before accessing parsed data.
- **Truncaion**: Break long inputs into chunks; merge results in application code.
- **Enums**: Force lowercase or normalize values before validation to avoid casing errors.

*Structure is the cage that holds the chaos of language. Let no field remain undefined.*