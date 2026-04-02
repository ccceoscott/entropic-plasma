#!/usr/bin/env node

/**
 * ╔══════════════════════════════════════════════════════════════╗
 * ║   SOVEREIGN MEMORY COMPACTOR v3.0 — Infinity Protocol       ║
 * ║   Phase 51 Apotheosis | Node 22 LTS | Zero-Dependency       ║
 * ╚══════════════════════════════════════════════════════════════╝
 *
 * Phases:
 *   1. Preflight   — env key loading, git checks, secret scan
 *   2. Ingestion   — MISSION_STATE.md, walkthrough.md, git context
 *   3. Compression — Gemini structured JSON summary
 *   4. KI Write    — Semantic Knowledge Item to ~/.gemini/antigravity
 *   5. State Reset — .agent/state.json + MISSION_STATE.md row append
 *   6. AI Commit   — Gemini-generated conventional commit message
 *   7. GitHub Sync — git add -A, commit, push to current branch
 *   8. Report      — Phase status summary table
 */

import fs from 'fs';
import path from 'path';
import os from 'os';
import { execSync } from 'child_process';

// ─── HELPERS ─────────────────────────────────────────────────────────────────

const GEMINI_URL = (key) =>
  `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${key}`;

const timer = () => {
  const start = Date.now();
  return () => `${((Date.now() - start) / 1000).toFixed(1)}s`;
};

const git = (cmd) => {
  try { return execSync(cmd, { encoding: 'utf8', stdio: 'pipe' }).trim(); }
  catch(e) { return ''; }
};

const safe = (fn, fallback = '') => { try { return fn(); } catch(e) { return fallback; } };

async function callGemini(apiKey, prompt, opts = {}) {
  const { maxTokens = 2048, temp = 0.1, jsonMode = false, retries = 1 } = opts;
  const body = {
    contents: [{ parts: [{ text: prompt }] }],
    generationConfig: {
      maxOutputTokens: maxTokens,
      temperature: temp,
      ...(jsonMode ? { responseMimeType: 'application/json' } : {})
    }
  };
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(GEMINI_URL(apiKey), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
      const data = await res.json();
      return data.candidates?.[0]?.content?.parts?.[0]?.text?.trim() || '';
    } catch(e) {
      if (attempt < retries) {
        console.warn(`  [↩️  Retry ${attempt + 1}] Gemini call failed — retrying...`);
        await new Promise(r => setTimeout(r, 1500));
      } else { throw e; }
    }
  }
}

// ─── GITIGNORE GAP ENFORCEMENT ───────────────────────────────────────────────

function enforceGitignore(projectRoot) {
  const gitignorePath = path.join(projectRoot, '.gitignore');
  const noisePatterns = [
    'tests/e2e/results/',
    'tests/e2e/html-report/',
    'playwright-report/',
    '.playwright/',
    'test-results/',
  ];
  let existing = fs.existsSync(gitignorePath) ? fs.readFileSync(gitignorePath, 'utf8') : '';
  const additions = noisePatterns.filter(p => !existing.includes(p));
  if (additions.length > 0) {
    existing += `\n# Auto-added by finalize_session.mjs\n${additions.join('\n')}\n`;
    fs.writeFileSync(gitignorePath, existing, 'utf8');
    console.log(`  -> .gitignore: added ${additions.length} noise pattern(s) [${additions.map(p => p.trim()).join(', ')}]`);
  }
}

// ─── SECRET SCAN ─────────────────────────────────────────────────────────────

function scanForSecrets(projectRoot) {
  const patterns = [
    /AIza[0-9A-Za-z\\-_]{35}/,            // Google API keys
    /AKIA[0-9A-Z]{16}/,                    // AWS Access Key IDs
    /sk-[a-zA-Z0-9]{32,}/,                // OpenAI
    /ghp_[a-zA-Z0-9]{36}/,               // GitHub Personal Access Tokens
    /-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----/, // Private keys
    /firebaseConfig\s*=\s*\{[^}]*apiKey:\s*["'][^"']{20,}/s, // Firebase inline config
  ];
  const staged = git('git diff --cached --name-only');
  if (!staged) return { clean: true, hits: [] };

  const hits = [];
  for (const file of staged.split('\n').filter(Boolean)) {
    const full = path.join(projectRoot, file);
    if (!fs.existsSync(full)) continue;
    const ext = path.extname(file).toLowerCase();
    if (['.png', '.jpg', '.zip', '.mp4', '.webp', '.ico'].includes(ext)) continue;
    try {
      const content = fs.readFileSync(full, 'utf8');
      for (const pattern of patterns) {
        if (pattern.test(content)) {
          hits.push({ file, pattern: pattern.toString().slice(1, 30) + '...' });
        }
      }
    } catch(e) {}
  }
  return { clean: hits.length === 0, hits };
}

// ─── SEMANTIC TAG DETECTION ──────────────────────────────────────────────────

function detectDomainTags(changedFiles) {
  const tags = new Set(['context-compaction', 'infinity-protocol']);
  const rules = [
    [/firebase\.json|firestore\.rules|\.firebaserc/, 'firebase-hosting'],
    [/functions\/src/, 'cloud-functions'],
    [/\.spec\.ts|\.test\.ts|e2e\//, 'e2e-testing'],
    [/src\/app\/components/, 'react-components'],
    [/src\/app\/contexts/, 'react-context'],
    [/src\/app\/App\.tsx/, 'app-root'],
    [/styles|\.css|tailwind/, 'styling'],
    [/package\.json|tsconfig/, 'build-config'],
    [/\.agent\/|MISSION_STATE|walkthrough/, 'protocol-governance'],
    [/auth|Auth/, 'authentication'],
    [/maps|Maps|Places/, 'google-maps'],
    [/analytics|Analytics/, 'analytics'],
    [/landing\/|index\.html/, 'landing-page'],
  ];
  for (const [pattern, tag] of rules) {
    if (pattern.test(changedFiles)) tags.add(tag);
  }
  return Array.from(tags);
}

// ─── MISSION_STATE AUTO-APPEND ───────────────────────────────────────────────

function appendMissionStateRow(missionStatePath, summary, branchName) {
  const dateStr = new Date().toISOString().replace('T', ' ').slice(0, 16) + ' UTC';
  const shortSummary = summary.split('\n')[0].slice(0, 120);
  const row = `\n| ${dateStr} | ${branchName} | ${shortSummary} |`;

  let content = fs.existsSync(missionStatePath)
    ? fs.readFileSync(missionStatePath, 'utf8')
    : '# MISSION STATE\n\n';

  // Append Optimization History table if not present
  if (!content.includes('## Optimization History')) {
    content += '\n\n## Optimization History\n| Timestamp | Branch | Summary |\n|---|---|---|';
  }
  content += row;
  fs.writeFileSync(missionStatePath, content, 'utf8');
}

// ─── SMART COMMIT TYPE DETECTION ─────────────────────────────────────────────

function detectCommitType(changedFiles) {
  if (/fix|bug|error|crash|broken|hotfix/i.test(changedFiles)) return 'fix';
  if (/refactor|cleanup|reorganiz|rename/i.test(changedFiles)) return 'refactor';
  if (/test|spec|e2e/i.test(changedFiles)) return 'test';
  if (/docs|README|MISSION_STATE|walkthrough/i.test(changedFiles)) return 'docs';
  if (/package\.json|tsconfig|vite\.config|webpack/i.test(changedFiles)) return 'chore';
  return 'feat';
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function run() {
  const sessionStart = Date.now();
  const projectRoot = process.cwd();
  const projectName = path.basename(projectRoot);
  const phaseStatus = {};

  console.log('\n╔══════════════════════════════════════════════════════════╗');
  console.log(`║  🧙 SOVEREIGN MEMORY COMPACTOR v3.0                      ║`);
  console.log(`║  Project: ${projectName.padEnd(46)}║`);
  console.log(`║  Time:    ${new Date().toISOString().replace('T', ' ').slice(0, 16).padEnd(46)}║`);
  console.log('╚══════════════════════════════════════════════════════════╝');

  // ── PHASE 0: PREFLIGHT ───────────────────────────────────────────────────
  const t0 = timer();
  process.stdout.write('\n[0/7] 🔑 Preflight — loading keys & scanning secrets...');

  // Key loading
  if (!process.env.GEMINI_API_KEY) {
    const envPaths = [
      path.join(projectRoot, '.env.local'),
      path.join(projectRoot, '.env'),
      path.join(os.homedir(), '.env.local'),
      path.join(os.homedir(), '.zshenv'),
    ];
    for (const ep of envPaths) {
      if (!fs.existsSync(ep)) continue;
      const match = fs.readFileSync(ep, 'utf8').match(/^GEMINI_API_KEY=(.+)$/m);
      if (match) {
        process.env.GEMINI_API_KEY = match[1].trim().replace(/^['"]|['"]$/g, '');
        process.stdout.write(` key from ${path.basename(ep)}`);
        break;
      }
    }
  }

  const geminiApiKey = process.env.GEMINI_API_KEY;
  if (!geminiApiKey) {
    console.error('\n[🚨] GEMINI_API_KEY missing. Add to .env.local or ~/.zshenv');
    process.exit(1);
  }

  // Enforce .gitignore patterns
  enforceGitignore(projectRoot);

  // Secret scan
  const scanResult = scanForSecrets(projectRoot);
  if (!scanResult.clean) {
    console.error('\n\n[🚨 SECURITY BLOCK] Potential secrets detected in staged files:');
    scanResult.hits.forEach(h => console.error(`  ⛔ ${h.file} (pattern: ${h.pattern})`));
    console.error('Resolve before committing. Run dv scan-secrets for full audit.');
    process.exit(2);
  }

  phaseStatus[0] = `✅ ${t0()}`;
  console.log(` ${phaseStatus[0]}`);

  // ── PHASE 1: INGESTION ────────────────────────────────────────────────────
  const t1 = timer();
  process.stdout.write('[1/7] 📥 Ingesting memory sources...');

  const agentDir = path.join(projectRoot, '.agent');
  if (!fs.existsSync(agentDir)) fs.mkdirSync(agentDir, { recursive: true });

  const missionStatePath  = path.join(projectRoot, 'MISSION_STATE.md');
  const walkthroughPath   = path.join(projectRoot, 'walkthrough.md');
  const agentStatePath    = path.join(agentDir, 'state.json');

  if (!fs.existsSync(missionStatePath))
    fs.writeFileSync(missionStatePath, '# MISSION STATE\n\nNo state recorded yet.', 'utf8');
  if (!fs.existsSync(agentStatePath))
    fs.writeFileSync(agentStatePath, JSON.stringify({
      system_phase: 'Initialization', active_blockers: [], current_focus: 'Pending',
      domain_tags: ['architecture'], completed_today: 0
    }, null, 2), 'utf8');

  const missionState  = fs.readFileSync(missionStatePath, 'utf8');
  const walkthrough   = fs.existsSync(walkthroughPath)
    ? fs.readFileSync(walkthroughPath, 'utf8').slice(0, 2000)
    : '(no walkthrough.md found)';
  const agentState    = fs.readFileSync(agentStatePath, 'utf8');

  const branchName    = git('git rev-parse --abbrev-ref HEAD') || 'main';
  const lastCommits   = git('git log --oneline -5') || '(no commits)';
  const stagedStat    = git('git diff --cached --stat') || '';
  const unstagedStat  = git('git diff --stat') || '';
  const untrackedFiles = git('git ls-files --others --exclude-standard') || '';
  const allChangedFiles = [stagedStat, unstagedStat, untrackedFiles].join('\n');
  const linesChanged  = safe(() => {
    const m = (stagedStat + unstagedStat).match(/(\d+) insertions.*?(\d+) deletions/);
    return m ? `+${m[1]}/-${m[2]}` : 'n/a';
  });

  phaseStatus[1] = `✅ ${t1()} | branch:${branchName} | Δ${linesChanged}`;
  console.log(` ${phaseStatus[1]}`);

  // ── PHASE 2: GEMINI COMPRESSION ───────────────────────────────────────────
  const t2 = timer();
  process.stdout.write('[2/7] 🤖 Gemini compression...');

  const compressionPrompt = `You are the Infinity Protocol Memory Compactor.
Summarize the following session state into a dense, structured knowledge item.
Focus on: fixed architectural decisions, resolved blockers, established patterns, and anti-patterns to avoid.

=== MISSION_STATE.md ===
${missionState.slice(0, 3000)}

=== walkthrough.md (last 2000 chars) ===
${walkthrough}

=== .agent/state.json ===
${agentState}

=== BRANCH: ${branchName} | RECENT COMMITS ===
${lastCommits}

=== STAGED CHANGES ===
${stagedStat || '(clean)'}

=== UNSTAGED CHANGES ===
${unstagedStat || '(clean)'}

Output a raw JSON object — NO markdown, NO backticks, NO prose:
{
  "markdown_summary": "High-density markdown. Include: what was accomplished, key decisions, patterns established, anti-patterns documented. Min 200 words.",
  "refined_domain_tags": ["tag1", "tag2"],
  "architectural_score": 7,
  "next_session_priorities": ["priority 1", "priority 2", "priority 3"]
}`;

  let parsedContent = {};
  let summaryMarkdown = `Session on ${new Date().toISOString().split('T')[0]}`;

  try {
    let raw = await callGemini(geminiApiKey, compressionPrompt, { maxTokens: 2048, temp: 0.1, retries: 1 });
    // Strip markdown fences if Gemini wraps response
    raw = raw.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/i, '').trim();
    try {
      parsedContent = JSON.parse(raw);
    } catch(parseErr) {
      // Fallback: extract fields via regex when Gemini embeds unescaped newlines
      const summaryMatch = raw.match(/"markdown_summary"\s*:\s*"([\s\S]+?)(?:",\s*"\w|\s*"\s*})/);
      const tagsMatch    = raw.match(/"refined_domain_tags"\s*:\s*\[([^\]]+)\]/);
      const scoreMatch   = raw.match(/"architectural_score"\s*:\s*(\d+)/);
      const priMatch     = raw.match(/"next_session_priorities"\s*:\s*\[([^\]]+)\]/);
      parsedContent = {
        markdown_summary: summaryMatch?.[1]?.replace(/\\n/g, '\n') || '',
        refined_domain_tags: tagsMatch ? tagsMatch[1].match(/"([^"]+)"/g)?.map(t => t.replace(/"/g, '')) || [] : [],
        architectural_score: scoreMatch ? parseInt(scoreMatch[1]) : 5,
        next_session_priorities: priMatch ? priMatch[1].match(/"([^"]+)"/g)?.map(t => t.replace(/"/g, '')) || [] : [],
      };
      phaseStatus[2] = `⚠️  ${t2()} | regex-extracted (JSON malformed)`;
    }
    if (!phaseStatus[2]) {
      summaryMarkdown = parsedContent.markdown_summary || summaryMarkdown;
      phaseStatus[2] = `✅ ${t2()} | score:${parsedContent.architectural_score || '?'}/10`;
    } else {
      summaryMarkdown = parsedContent.markdown_summary || summaryMarkdown;
    }
  } catch(e) {
    phaseStatus[2] = `⚠️  ${t2()} | fallback (${e.message?.slice(0, 40)})`;
  }
  console.log(` ${phaseStatus[2]}`);

  // ── PHASE 3: KI WRITE ─────────────────────────────────────────────────────
  const t3 = timer();
  process.stdout.write('[3/7] 💾 Writing Knowledge Item...');

  const dateStr     = new Date().toISOString().split('T')[0];
  const fileId      = `session_${dateStr}_${Date.now()}`;
  const appDataDir  = path.join(os.homedir(), '.gemini', 'antigravity', 'knowledge', 'session_summaries');
  const artifactsDir = path.join(appDataDir, 'artifacts');
  if (!fs.existsSync(artifactsDir)) fs.mkdirSync(artifactsDir, { recursive: true });

  const artifactPath  = path.join(artifactsDir, `${fileId}.md`);
  const metadataPath  = path.join(appDataDir, 'metadata.json');

  const nextPriorities = (parsedContent.next_session_priorities || []).map(p => `- ${p}`).join('\n');
  const semanticTags   = detectDomainTags(allChangedFiles);
  const domainTags     = Array.from(new Set([
    ...(parsedContent.refined_domain_tags || []),
    ...semanticTags,
    `branch:${branchName}`,
    `project:${projectName}`,
  ]));

  fs.writeFileSync(artifactPath, [
    `# Session Compaction: ${dateStr}`,
    `**Project:** ${projectName} | **Branch:** ${branchName} | **Score:** ${parsedContent.architectural_score || '?'}/10`,
    `**Tags:** ${domainTags.join(', ')}`,
    '',
    summaryMarkdown,
    '',
    nextPriorities ? `## Next Session Priorities\n${nextPriorities}` : '',
  ].join('\n'));

  let metadataArray = [];
  if (fs.existsSync(metadataPath)) {
    try { metadataArray = JSON.parse(fs.readFileSync(metadataPath, 'utf8')); } catch(e) {}
    if (!Array.isArray(metadataArray)) metadataArray = [];
  }
  metadataArray.push({
    fileId, project: projectName, branch: branchName,
    summary: `${projectName} session ${dateStr}`,
    domain_tags: domainTags,
    priority_score: parsedContent.architectural_score || 5,
    last_accessed: new Date().toISOString(),
    artifact_paths: [`session_summaries/artifacts/${fileId}.md`],
    next_priorities: parsedContent.next_session_priorities || [],
  });
  fs.writeFileSync(metadataPath, JSON.stringify(metadataArray, null, 2));

  phaseStatus[3] = `✅ ${t3()} | ${fileId}.md`;
  console.log(` ${phaseStatus[3]}`);

  // ── PHASE 4: STATE RESET + MISSION_STATE APPEND ───────────────────────────
  const t4 = timer();
  process.stdout.write('[4/7] 🔁 Resetting state & updating MISSION_STATE...');

  // Purge scratchpads
  for (const p of [path.join(os.tmpdir(), 'SCRATCHPAD.md'), '/tmp/SCRATCHPAD.md']) {
    if (fs.existsSync(p)) fs.unlinkSync(p);
  }

  // Reset agent state
  try {
    const rawState = JSON.parse(agentState);
    rawState.completed_today = 0;
    rawState.active_blockers = [];
    rawState.previous_session_reference = artifactPath;
    rawState.last_compaction = new Date().toISOString();
    fs.writeFileSync(agentStatePath, JSON.stringify(rawState, null, 2));
  } catch(e) {}

  // Append row to MISSION_STATE.md Optimization History
  appendMissionStateRow(missionStatePath, summaryMarkdown, branchName);

  phaseStatus[4] = `✅ ${t4()}`;
  console.log(` ${phaseStatus[4]}`);

  // ── PHASE 5: AI COMMIT MESSAGE ────────────────────────────────────────────
  const t5 = timer();
  process.stdout.write('[5/7] ✍️  Generating AI commit message...');

  const commitType  = detectCommitType(allChangedFiles);
  const fallbackMsg = `${commitType}(${projectName}): finalize session ${dateStr} — automated compaction`;

  let commitMessage = fallbackMsg;

  try {
    const commitPrompt = `You are an expert software engineer writing a GitHub commit message.
Produce a rich, detailed conventional commit message from the session data below.

RULES:
- Line 1: "type(scope): imperative summary" (max 72 chars, no period)
- Line 2: blank
- Lines 3+: "- " bullet points, max 8, each describing a specific technical change
- Types: feat | fix | chore | refactor | docs | perf | test
- Scope: infer from project name or changed area
- NO markdown, NO backticks, NO code fences, NO trailing whitespace
- Output ONLY the commit message, nothing else

SESSION SUMMARY (excerpt):
${summaryMarkdown.slice(0, 1500)}

CHANGED FILES:
${allChangedFiles.slice(0, 800) || '(staged only)'}

BRANCH: ${branchName} | PROJECT: ${projectName}`;

    const aiMsg = await callGemini(geminiApiKey, commitPrompt, { maxTokens: 512, temp: 0.15, retries: 1 });
    if (aiMsg && aiMsg.length > 15 && aiMsg.split('\n')[0].includes(':')) {
      commitMessage = aiMsg;
    }
  } catch(e) {
    phaseStatus[5] = `⚠️  ${t5()} | fallback`;
  }

  if (!phaseStatus[5]) phaseStatus[5] = `✅ ${t5()} | "${commitMessage.split('\n')[0].slice(0, 55)}..."`;
  console.log(` ${phaseStatus[5]}`);

  // ── PHASE 6: GITHUB SYNC ─────────────────────────────────────────────────
  const t6 = timer();
  process.stdout.write('[6/7] 🐙 GitHub sync...');

  try {
    execSync('git add -A', { stdio: 'pipe' });
    const staged = git('git diff --cached --name-only');
    if (!staged) {
      phaseStatus[6] = `⏭  ${t6()} | nothing to commit`;
    } else {
      execSync(`git commit -m ${JSON.stringify(commitMessage)} --no-verify`, { stdio: 'pipe' });
      execSync(`git push origin ${branchName}`, { stdio: 'pipe' });
      const sha = git('git rev-parse --short HEAD');
      phaseStatus[6] = `✅ ${t6()} | ${sha} → origin/${branchName}`;
    }
  } catch(e) {
    const msg = e.message || '';
    if (msg.includes('nothing to commit')) {
      phaseStatus[6] = `⏭  ${t6()} | nothing to commit`;
    } else {
      phaseStatus[6] = `⚠️  ${t6()} | ${msg.slice(0, 60)}`;
    }
  }
  console.log(` ${phaseStatus[6]}`);

  // ── PHASE 7: REPORT ──────────────────────────────────────────────────────
  const totalTime = `${((Date.now() - sessionStart) / 1000).toFixed(1)}s`;

  console.log('\n╔══════════════════════════════════════════════════════════╗');
  console.log('║  📊 SESSION COMPACTION REPORT                            ║');
  console.log('╠══════════════════════════════════════════════════════════╣');
  console.log(`║  [0] Preflight    ${phaseStatus[0]?.padEnd(40)}║`);
  console.log(`║  [1] Ingestion    ${phaseStatus[1]?.padEnd(40)}║`);
  console.log(`║  [2] Compression  ${phaseStatus[2]?.padEnd(40)}║`);
  console.log(`║  [3] KI Write     ${phaseStatus[3]?.padEnd(40)}║`);
  console.log(`║  [4] State Reset  ${phaseStatus[4]?.padEnd(40)}║`);
  console.log(`║  [5] AI Commit    ${phaseStatus[5]?.padEnd(40)}║`);
  console.log(`║  [6] GitHub Sync  ${phaseStatus[6]?.padEnd(40)}║`);
  console.log('╠══════════════════════════════════════════════════════════╣');
  console.log(`║  Total: ${totalTime.padEnd(49)}║`);
  if (parsedContent.next_session_priorities?.length) {
    console.log('╠══════════════════════════════════════════════════════════╣');
    console.log('║  🎯 Next Session Priorities:                             ║');
    parsedContent.next_session_priorities.slice(0, 3).forEach(p => {
      console.log(`║    • ${p.slice(0, 52).padEnd(53)}║`);
    });
  }
  console.log('╚══════════════════════════════════════════════════════════╝\n');
}

run().catch((e) => {
  console.error('\n[🚨 FATAL]', e.message);
  process.exit(1);
});
