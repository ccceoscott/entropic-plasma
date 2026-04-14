---
name: llm-structured-output
description: LLM structured output engineer — enforces JSON schema constraints, Zod/Pydantic validation on model responses, and retry logic for malformed outputs.
phase: "209"
category: ai
tags: ["llm", "structured-output", "json-schema", "zod", "validation"]
---

# LLM Structured Output (R.A.P.S.) — Phase 207.16

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
