/**
 * Infinity Protocol — Gemini Model Registry v1.0
 * ─────────────────────────────────────────────────────────────
 * SINGLE SOURCE OF TRUTH for all Gemini model IDs.
 * 
 * ⚠️  NEVER hardcode model strings in application code.
 *     Always import from this file.
 * 
 * Lifecycle:
 *   - Run `dv gemini-check`  to compare against live API
 *   - Run `dv gemini-audit`  to find hardcoded model strings
 *   - Run `dv gemini-upgrade` to apply the latest stable recommendation
 * 
 * As of: 2026-03-20
 * Source: https://ai.google.dev/gemini-api/docs/models
 */

// ─── Tier 1: Stable Production (GA) ──────────────────────────
// Use these for ALL production workloads.

/** @stable Best reasoning + code. 1M context. GA Jun 2025. EOL Jun 2026. */
export const GEMINI_PRO     = 'gemini-2.5-pro'         as const;

/** @stable Best price/performance. Fast, reasoning-capable. GA Jun 2025. */
export const GEMINI_FLASH   = 'gemini-2.5-flash'       as const;

/** @stable Embedding model. 3072-dim, MRL truncation. GA Jul 2025. */
export const GEMINI_EMBED   = 'gemini-embedding-001'   as const;

// ─── Tier 2: Preview (Early Adopter) ─────────────────────────
// Higher capability, may have breaking changes before GA.
// Pin to explicit preview IDs — never use `latest` in preview tier.

/** @preview Most capable reasoning. Launched Feb 2026. */
export const GEMINI_3_PRO_PREVIEW       = 'gemini-3.1-pro-preview'       as const;

/** @preview Fastest + cheapest. 40% cheaper than 2.5-flash. Launched Mar 3 2026. */
export const GEMINI_3_FLASH_LITE_PREVIEW = 'gemini-3.1-flash-lite-preview' as const;

// ─── EOL — Forbidden in New Code ─────────────────────────────
// Kept here for migration tracking only. Will throw at runtime if used.

/** @deprecated EOL Jun 1 2026. Migrate to GEMINI_FLASH immediately. */
export const GEMINI_2_FLASH_EOL = 'gemini-2.0-flash' as const;

/** @deprecated Shutdown Jan 2026. Any usage must be replaced with GEMINI_EMBED. */
export const TEXT_EMBEDDING_004_EOL = 'text-embedding-004' as const;

// ─── Role-Based Defaults ─────────────────────────────────────
// These are the canonical choices for each system role.
// Swap stable ↔ preview here when a preview model reaches GA.

export const GEMINI_MODELS = {
  /** Chat completions, reasoning, function calling */
  chat:           GEMINI_FLASH,

  /** Complex analysis, long-context (>200K), architecture decisions */
  reasoning:      GEMINI_PRO,

  /** All embedding tasks — RETRIEVAL_QUERY, RETRIEVAL_DOCUMENT, CLASSIFICATION, SEMANTIC_SIMILARITY */
  embedding:      GEMINI_EMBED,

  /** System prompts / Zoltan persona — balance of speed + quality */
  persona:        GEMINI_FLASH,

  /** Email subject classification — cost-sensitive, high volume */
  classification: GEMINI_FLASH,

  /** Admin / background analysis tasks (batch, non-real-time) */
  batch:          GEMINI_PRO,

  /** Light UI generation, suggestions, autocomplete — lowest latency */
  lite:           GEMINI_3_FLASH_LITE_PREVIEW,
} as const;

export type GeminiModelRole = keyof typeof GEMINI_MODELS;
export type GeminiModelId   = (typeof GEMINI_MODELS)[GeminiModelRole];

// ─── Endpoint Helpers ─────────────────────────────────────────

const BASE = 'https://generativelanguage.googleapis.com/v1beta';

export const GEMINI_ENDPOINTS = {
  generateContent: (model: string, key: string) =>
    `${BASE}/models/${model}:generateContent?key=${key}`,
  embedContent: (model: string, key: string) =>
    `${BASE}/models/${model}:embedContent?key=${key}`,
  listModels: (key: string) =>
    `${BASE}/models?key=${key}`,
} as const;

// ─── Runtime EOL Guard ────────────────────────────────────────

const FORBIDDEN_MODELS = new Set<string>([GEMINI_2_FLASH_EOL, TEXT_EMBEDDING_004_EOL]);

/**
 * Guard against accidental use of deprecated models.
 * Call at the top of any service that accepts a model ID parameter.
 */
export function assertModelAllowed(modelId: string): void {
  if (FORBIDDEN_MODELS.has(modelId)) {
    throw new Error(
      `[GeminiModels] FORBIDDEN: "${modelId}" is EOL and must not be used. ` +
      `See src/lib/geminiModels.ts for current model registry.`
    );
  }
}

// ─── Upgrade Metadata ─────────────────────────────────────────

/** Run `dv gemini-check` to compare this against the live API. */
export const MODEL_REGISTRY_VERSION = '2026-03-20';

export const EOL_WARNINGS: Record<string, { deadline: string; migration: string }> = {
  [GEMINI_2_FLASH_EOL]:       { deadline: '2026-06-01', migration: `Use ${GEMINI_FLASH}` },
  [TEXT_EMBEDDING_004_EOL]:   { deadline: '2026-01-01', migration: `Use ${GEMINI_EMBED}` },
  'gemini-3-pro-preview':     { deadline: '2026-03-09', migration: `Use ${GEMINI_3_PRO_PREVIEW}` },
};
