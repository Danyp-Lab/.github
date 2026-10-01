# Security Policy

## 🛡️ Responsible Disclosure
We treat homelab security with the same rigor as enterprise production environments. If you identify a security issue, vulnerability, or accidental secret leak across any repository in the **Danyp-Lab** organization:

1. **DO NOT** open a public GitHub issue.
2. Report the vulnerability privately via **[GitHub Private Vulnerability Reporting](https://github.com/Danyp-Lab/.github/security/advisories/new)** (enabled across all repos).
3. Alternatively, contact the maintainer directly via email: `daniel.pahlavan@gmail.com`.

## 📋 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.x     | :white_check_mark: |
| 1.x     | :x:                |

---

## 🔒 Secret Management Policy
- **Zero Credentials in Git**: Never push `.env` files containing live secrets. Use `.env.example` templates with placeholder values.
- If a secret is ever accidentally pushed:
  - It must be considered **compromised immediately**.
  - Rotate the credential at the upstream source before removing it from git history.
  - Purge git history using `git-filter-repo` or BFG Repo-Cleaner if necessary.

---

## 🚨 Security Defaults
- Public repositories must have **Secret Scanning** and **Push Protection** enabled.
- Default branch protection prevents force pushes and unauthorized merges.
- Docker containers run with non-root UID/GID where supported and read-only root filesystems where practical.
