## 📌 Description of Changes
<!-- Clearly summarize what this PR changes, adds, or fixes. -->

- 

## 🎯 Component Affected
- [ ] Docker Compose Stack (`docker-services`)
- [ ] Network / VLAN / Firewall (`network-routing`)
- [ ] Base OS / Infrastructure (`infra-core`)
- [ ] Monitoring / Alerting (`monitoring-stack`)
- [ ] CI/CD / Workflows / Documentation (`.github`)

## 🛡️ DevSecOps & Security Checklist
- [ ] **No Secrets Committed**: Verified no `.env`, passwords, private keys, tokens, or plaintext credentials are included.
- [ ] **Sanitized Configuration**: Any public domain names or external IPs have been scrubbed or parameterized.
- [ ] **Syntax & Validation**:
  - [ ] `docker compose -f <file> config` validates cleanly (if docker-related).
  - [ ] Shell scripts formatted and passed `shellcheck` (if bash-related).
  - [ ] YAML passed linter without indentation errors.
- [ ] **Network Exposure Check**: Verified ports exposed to host/WAN adhere to least-privilege principles.

## 🧪 Testing Performed
<!-- Describe how you tested this change in your dev/staging homelab environment. -->
