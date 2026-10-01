# Contributing to Danyp-Lab

Thank you for your interest in contributing! Whether you are proposing a new Docker service, tuning firewall rules, or optimizing automation scripts, please review this guide.

---

## 🛠️ Contribution Workflow

1. **Branching Strategy**:
   - Create a feature branch off `main`: `feat/service-name`, `fix/networking-issue`, or `chore/linting`.
   - Never commit directly to `main`.
2. **Commit Conventions**:
   - Follow [Conventional Commits](https://www.conventionalcommits.org/):
     - `feat:` New service, playbook, or integration
     - `fix:` Bug fix, syntax fix, or configuration correction
     - `chore:` Dependency update, cleanup, or documentation
     - `sec:` Security hardening, secret rotation, or permission updates
3. **Local Validation**:
   - Run `docker compose -f <file> config` to ensure YAML validity.
   - Run `shellcheck <script.sh>` on all bash scripts.
   - Run `yamllint` on all Kubernetes/Compose manifests.
4. **Pull Requests**:
   - Open a PR targeting `main`.
   - Fill out the PR template checklist completely.
   - Ensure all automated GitHub Action checks pass.
