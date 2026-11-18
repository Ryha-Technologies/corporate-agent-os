# Release process

1. Update `VERSION`, add a `## [x.y.z] — date` section to `CHANGELOG.md`, and make sure `README.md` mentions the version (the structure validator checks all three agree with the Power manifest).
2. Run `python scripts/package/build_release.py --out dist`. It regenerates adapters, the Power and rendered docs, runs all validators (aborting on failure), zips the repository and the Power, re-opens both archives, verifies entry counts and `plugin.json`, and writes `SHA256SUMS.txt` and `release-manifest.json`.
3. Extract `dist/corporate-agent-os-final.zip` to a temporary directory and run `python scripts/validate/run_all.py` and `python -m pytest -q` there.
4. Tag `vX.Y.Z`, create the GitHub release, attach both zips and `SHA256SUMS.txt`, paste the changelog section, and link the latest `evaluations/benchmark-reports/` entry (or state that none was run).
5. Never publish a release while any validator fails, and never describe the release with quality labels the gate evidence does not support.

Pre-release labels (`-beta.N`) are allowed; the project stays below 1.0.0 until the criteria in the README roadmap are met.
