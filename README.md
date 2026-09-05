# DevelopTool — ADL Agent Engineering Platform

**Status:** Resurrection target (spec-first)  
**Lab:** [Atomic Dream Labs / beyond-repair](https://github.com/beyond-repair)  
**License:** See repository license file if present; otherwise treat as research prototype.

---

## Purpose

DevelopTool is the product-facing name for an **agent-native engineering environment**: repository-scale understanding, constitutional gates, and assisted change — not another thin chat wrapper around a single model API.

This repository holds the **platform thesis, scope, and integration map**. Runtime intelligence is intended to compose existing lab systems rather than reimplement them.

```
Developer intent
       ↓
DevelopTool (this repo — UX, workflows, packaging)
       ↓
sunder          → local-first coding agent + gates
sovereign-clean-room → VSA / clean-room memory kernel
ADL census/graph    → portfolio truth & claim surfaces
```

---

## Why this exists

Commercial tools (Cursor, Claude Code, Codex, Windsurf, OpenHands, and peers) proved demand for AI-assisted development. Gaps remain around:

| Gap | DevelopTool stance |
|-----|--------------------|
| Repo portfolio awareness | Integrate ADL census / capability matrix / repo graph |
| Unbounded agent actions | Prefer constitutional / claim-capped gates (sunder lineage) |
| Opaque memory | Prefer explicit VSA / clean-room boundaries |
| Single-repo tunnel vision | Design for multi-repo lab workflows |

---

## Scope (claim-capped)

**In scope**

- Workflow definitions for plan → edit → test → review
- CLI / IDE extension *contracts* (interfaces, not vapor features)
- Integration adapters to `sunder` and `sovereign-clean-room`
- Documentation of operator queues and safety boundaries

**Out of scope (do not claim)**

- Full IDE replacement shipped from this README alone
- Autonomous production deploys without human approval
- AGI or unsupervised multi-hour agency

---

## Relationship to the portfolio

| System | Role |
|--------|------|
| [sunder](https://github.com/beyond-repair/sunder) | Agent runtime |
| [sovereign-clean-room](https://github.com/beyond-repair/sovereign-clean-room) | Memory / VSA kernel |
| [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) | Lab constitution |
| [ADL-Portfolio-Census](https://github.com/beyond-repair/ADL-Portfolio-Census) | Inventory truth |
| [RepoRover-](https://github.com/beyond-repair/RepoRover-) | Portfolio intelligence UI path |

---

## Roadmap (practical)

1. **Spec lock** — operator workflows and non-negotiable safety rules  
2. **Thin CLI** — invoke sunder against a target repo with gated apply  
3. **Read-only intelligence** — surface census/graph health for the target  
4. **Optional IDE surface** — only after CLI is stable  

---

## Contributing

Issues and PRs should reference a concrete workflow or adapter. Speculative “full platform” dumps without integration points will be declined.

---

*Atomic Dream Labs — rewrite · build · transcend*
