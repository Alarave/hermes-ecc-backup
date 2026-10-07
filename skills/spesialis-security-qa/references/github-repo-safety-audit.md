# GitHub Repo Safety Audit

Workflow for analyzing unknown GitHub repositories for safety before cloning or installing, tailored to the user's security posture.

## Procedure: Auditing a Repository
1. **Identify the Core Purpose:** Determine what the tool claims to do (e.g., CLI fixer, generator, proxy).
2. **Scan for Credential Harvesting:**
   - Does it prompt for passwords, tokens, or API keys directly in the terminal? (Major red flag).
   - Does it run hidden browser instances (like `camoufox`) to bypass OAuth flows?
   - If it claims to interact with accounts (e.g., Google, GitHub), does it use official OAuth mechanisms or does it ask for raw credentials?
3. **Verify Execution Context:** 
   - Check the dependencies (e.g., `requirements.txt`, `package.json`).
   - Does it execute obfuscated code, download unverified binaries, or send data to external unknown servers?
4. **Issue a Verdict:**
   - **Unsafe:** Explicitly state the security warning. Do not proceed with installation. Provide the safe manual alternative (e.g., "Delete cache manually and use official OAuth").
   - **Safe:** State that it is safe, briefly summarize why (e.g., "Uses standard open-source tools, no credential requests, no external data exfiltration"), and proceed to clone or install if requested.

## Pitfalls
- **Implicitly Trusting "Open Source":** Just because code is on GitHub does not mean it is safe. CLI scripts that ask for passwords directly (like `antigravity-fixer`) are high-risk for credential theft, even if they claim "in-memory only". Always flag direct password prompts as unsafe.
- **Executing Before Auditing:** Never run `git clone` or install a repository until the safety analysis is complete and the verdict is clearly communicated to the user.
