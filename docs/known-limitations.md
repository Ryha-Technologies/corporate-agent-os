# Known limitations (0.2.0)

Listed so nobody mistakes this build for more than it is.

## Not executed in this build
- **No model-driven benchmark has been run.** The regression dataset, rubrics and golden tasks exist; results are NOT_RUN. Quality of model behaviour on these skills is unmeasured.
- **Kiro CLI 3.3.0 live install performed** (agents listed and validated by the CLI). Kiro IDE, Claude Code and Codex have not loaded the files in a live session; format conformance there rests on official documentation.
- Linux and macOS: validators and the full test suite (including installer tests) pass in GitHub Actions on ubuntu-latest, windows-latest and macos-latest for Python 3.10 and 3.12; no interactive host run on those platforms.
- **No trademark database queries, SBOM generations or browser screenshot tests** were run; those are procedures the skills describe.

## Design limits
- Skills and agents are instructions. A model may ignore them. Independent review and human approval exist because of that.
- Write-scope enforcement is technical only on Kiro (`fs_write` matchers). On Claude Code and Codex it is an instruction verified by the code reviewer.
- Codex has no sub-agent configuration; delegation degrades to sequential passes and is disclosed as such.
- Kiro's DAG is planned up front and cannot change mid-run; the orchestrator plans the whole workflow before delegating.
- No browser tool is bundled for design QA; an MCP server must be configured by the user.
- The Kiro Power contains skills only. Kiro documents no Power component for agents, steering or hooks; those install into `.kiro/` separately.
- Claude Code plugin packaging (`.claude-plugin/plugin.json`) and Codex plugin packaging are not provided.
- The evaluation harness validates assets and writes report skeletons; it does not score transcripts.
- The minimal JSON Schema validator in `scripts/validate/common.py` supports the subset the repository uses; it is not a general implementation.
- Cost tracking depends on what the host exposes; where nothing is exposed the log says NOT_MEASURED.

## Content limits
- Role definitions are generalised from common technology-company practice; they are starting points to adapt, not research findings about any specific company.
- Trademark office references cover India, the US, the EU, the UK and WIPO; other jurisdictions must be added per project.
- Standards are cited by theme; section numbers must be verified against current publications before being quoted.
- Examples under `examples/` are illustrative specifications with placeholder values, not records of real projects.

## Platform volatility
Kiro, Claude Code and Codex changed formats several times in 2026. Everything here was verified on 2026-11-18 (`research/source-register.md`). Re-verify before upgrading a host or publishing.
