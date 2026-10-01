# Danyp-Lab 🌐🛠️

Welcome to **Danyp-Lab**, a self-hosted infrastructure, networking, and GitOps ecosystem designed for high availability, security isolation, and observability.

---

### 🏛️ Architecture & Ecosystem Overview

```
               [ Internet / Cloudflare / DNS ]
                              │
                              ▼
                   [ OPNsense / Edge Router ]
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
      [ DMZ / External Ingress ]     [ Trusted VLAN / Internal ]
         • Reverse Proxy (Traefik)      • Storage (TrueNAS / NFS)
         • Authelia / Authentik         • Core DNS & WireGuard
               │                             │
               └──────────────┬──────────────┘
                              ▼
                 [ Compute Nodes & Runtimes ]
                 • Docker Compose / Swarm / K3s
                 • Observability (Prometheus / Grafana / Loki)
                 • Automation (Ansible / CI/CD Runners)
```

---

### 💻 Core Tech Stack

| Category | Technologies & Tools |
| :--- | :--- |
| **Containers & Virtualization** | Docker, Docker Compose, Proxmox VE, LXC |
| **Networking & Routing** | OPNsense, WireGuard, VLAN Segmentation, Cloudflare Tunnels |
| **Reverse Proxy & Ingress** | Traefik / Nginx Proxy Manager, Tailscale |
| **Identity & Access** | Authentik / Authelia (SSO, 2FA, OIDC) |
| **Observability & Logging** | Prometheus, Grafana, Loki, Uptime Kuma, cAdvisor |
| **Storage & Backup** | TrueNAS CORE/SCALE, ZFS, Restic, BorgBackup |
| **CI/CD & GitOps** | GitHub Actions, Self-hosted Runners, Renovate/Dependabot |

---

### 📂 Repository Directory

| Repository | Purpose | Primary Stack |
| :--- | :--- | :--- |
| [`infra-core`](https://github.com/Danyp-Lab/infra-core) | Base OS configurations, Ansible playbooks, and hardware bootstrap | Ansible, Bash, Linux |
| [`network-routing`](https://github.com/Danyp-Lab/network-routing) | Firewall rules, DNS configs, WireGuard, and VLAN layouts | OPNsense, Unbound, WG |
| [`docker-services`](https://github.com/Danyp-Lab/docker-services) | Production service stack compose definitions and env templates | Docker Compose, Traefik |
| [`monitoring-stack`](https://github.com/Danyp-Lab/monitoring-stack) | Metrics scraping, log aggregation, and alerting dashboards | Prometheus, Grafana |
| [`.github`](https://github.com/Danyp-Lab/.github) | Org-wide health files, reusable workflows, and issue templates | GitHub Actions |

---

### 🔒 Security Baseline

- **Zero Clear-Text Secrets**: All secrets managed via environment vaults / SOPS / sealed secrets; never committed to git.
- **Least-Privilege Networking**: Strict inter-VLAN firewalls; services strictly bound to private/loopback bridges.
- **Continuous Validation**: Linters (`actionlint`, `yamllint`, `shellcheck`, `docker compose config`) run on every PR.
