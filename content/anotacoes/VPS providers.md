---
title: VPS providers
date: 2025-02-24
lastmod: 2026-02-20
---


## Summary

| Provider                          | Link                         | Brazil | Free Tier                          | Starting Price           | Pricing Model        |
| --------------------------------- | ---------------------------- | ------ | ---------------------------------- | ------------------------ | -------------------- |
| [AWS Lightsail](#aws-lightsail)   | https://aws.amazon.com       | ✅     | 3 months on select plans           | $3.50/mo                 | Fixed bundles        |
| [DigitalOcean](#digitalocean)     | https://www.digitalocean.com | ❌     | $200 credit / 60 days              | $4/mo                    | Per-second billing   |
| [exe.dev](#exedev)                | https://exe.dev              | ❌     | Free trial available               | $20/mo                   | Flat monthly         |
| [Fly.io](#flyio)                  | https://fly.io               | ❌     | Legacy free tier (deprecated)      | ~$2/mo                   | Pay-as-you-go        |
| [GCP Compute Engine](#gcp)        | https://cloud.google.com     | ✅     | 1 e2-micro forever + $300/90 days  | ~$3.50/mo (e2-micro)     | Per-second billing   |
| [Hetzner](#hetzner)               | https://www.hetzner.com      | ❌     | None                               | €3.79/mo                 | Hourly / monthly cap |
| [HostGator](#hostgator)           | https://www.hostgator.com.br | ✅     | None                               | R$ 25,89/mo              | Monthly              |
| [Hostinger](#hostinger)           | https://www.hostinger.com.br | ✅     | None                               | $4.99/mo (~R$ 29/mo)     | Monthly / annual     |
| [KingHost](#kinghost)             | https://king.host            | ✅     | None                               | R$ 29/mo                 | Monthly / quarterly  |
| [Locaweb](#locaweb)               | https://www.locaweb.com.br   | ✅     | None                               | R$ 15,90/mo              | Monthly / quarterly  |
| [Napoleon](#napoleon)             | https://napoleon.com.br      | ✅     | None                               | —                        | —                    |
| [Northflank](#northflank)         | https://northflank.com       | ❌     | 2 services + 2 DBs + 2 cron jobs   | ~$2.70/mo (pay-as-you-go)| Per-second billing   |
| [Oracle Cloud](#oracle-cloud)     | https://cloud.oracle.com     | ❌     | 4 ARM cores + 24 GB RAM forever    | $0/mo                    | Pay-as-you-go        |
| [Railway](#railway)               | https://railway.com          | ❌     | $5 credit / 30-day trial only      | $5/mo (Hobby)            | Usage-based          |
| [Vultr](#vultr)                   | https://www.vultr.com        | ✅     | None                               | $2.50/mo                 | Hourly / monthly cap |

> Brazil ✅ means the provider has a data center in Brazil or explicitly serves Brazilian customers.


## Providers

### AWS Lightsail

Simple, predictable VPS from AWS. Bundles compute, SSD, and bandwidth into a single monthly price, making it easier to estimate costs than EC2.

- **Free tier:** 3 months free on select bundles (Linux from $3.50/mo, containers from $10/mo, databases from $15/mo). Also 1 year free for 50 GB CDN and 5 GB object storage.
- **Starting price:** $3.50/mo (IPv6-only Linux) / $5/mo (with IPv4)
- **$5/mo plan:** 2 vCPU, 0.5 GB RAM, 20 GB SSD, 1 TB transfer
- **$7/mo plan:** 2 vCPU, 1 GB RAM, 40 GB SSD, 2 TB transfer
- **$12/mo plan:** 2 vCPU, 2 GB RAM, 60 GB SSD, 3 TB transfer
- **Pricing model:** Fixed monthly bundles; billed hourly on-demand at $0.0047/hr minimum
- **Data centers:** Multiple AWS regions worldwide (no Brazil-specific region for Lightsail)
- **Notes:** Simpler and cheaper than EC2 for small workloads. Excess data transfer starts at $0.09/GB.

---

### DigitalOcean

Developer-friendly cloud with a clean UI and predictable pricing. Known as Droplets.

- **Free tier:** $200 credit valid for 60 days for new accounts (credit card required)
- **Starting price:** $4/mo (Basic, 512 MB RAM) / $6/mo (1 GB RAM)
- **Entry plan (Basic):** 1 vCPU, 512 MB–1 GB RAM, 10–25 GiB SSD, 500 GiB–1 TiB transfer
- **Premium Intel (NVMe):** from $8/mo — 1 vCPU, 1 GB RAM, 35 GiB NVMe SSD, 1 TiB transfer
- **Premium AMD (NVMe):** from $7/mo — 1 vCPU, 1 GB RAM, 25 GiB NVMe SSD, 1 TiB transfer
- **Pricing model:** Per-second billing (since Jan 2026), monthly cap of 672 hours. Inbound bandwidth free; extra outbound at $0.01/GiB.
- **Data centers:** No Brazil data center
- **Notes:** Good documentation and ecosystem. No Brazil region is a downside for latency-sensitive Brazilian applications.

---

### exe.dev

Minimalist VM service focused on fast setup (zero to running in 1–2 minutes). Designed specifically for running tools like Claude Code.

- **Free tier:** Free trial available (check [exe.dev/docs/pricing](https://exe.dev/docs/pricing) for current terms)
- **Starting price:** $20/mo
- **Plan:** Up to 25 VMs sharing 2 CPUs and 8 GB RAM across the account; 25 GB disk
- **Pricing model:** Flat monthly subscription; resources shared across all VMs
- **Data centers:** Not disclosed
- **Notes:** Not a traditional dedicated VPS — resources (CPU/RAM) are shared across all your VMs. Includes built-in HTTPS proxy and instant DNS. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### Fly.io

Application hosting platform that deploys containers close to users globally. Billed per actual utilization.

- **Free tier:** Legacy free tier (3 shared-cpu-1x VMs + 3 GB storage) for accounts on deprecated plans. No permanent free tier for new accounts.
- **Starting price:** ~$2/mo for a shared-cpu-1x (256 MB RAM); full shared-cpu-1x at ~$2.02–$88.88/mo depending on RAM
- **Entry plan:** Shared CPU VMs; $5/GB/mo additional RAM; stopped machines charged only $0.15/GB/mo storage
- **Pricing model:** Pay-as-you-go based on actual utilization. Yearly reservations available at 40% discount.
- **Networking:** $2/mo dedicated IPv4; data transfer $0.02–$0.12/GB by region
- **Data centers:** Global (no Brazil-specific region)
- **Notes:** PaaS/container-focused, not a raw VPS. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### GCP

Google Cloud Platform's Compute Engine. Pay-as-you-go with a generous permanent free tier.

- **Free tier (always free):** 1 non-preemptible **e2-micro** instance/month (up to 720 hours) in select US regions; 30 GB HDD storage; 1 GB network egress/month
- **Welcome credit:** $300 credit valid for 90 days for new accounts
- **Starting price:** ~$0.0067/hr ($4.89/mo) for e2-micro outside free tier; n1-standard-1 from ~$0.0475/hr
- **Pricing model:** Per-second billing (1-minute minimum). Sustained-use discounts automatically applied.
- **Storage:** Standard storage from ~$0.026/GB/mo
- **Data centers:** Brazil (southamerica-east1, São Paulo), plus USA, Europe, Asia, and more (31 regions total)
- **Notes:** The always-free e2-micro is only available in specific US regions (not Brazil). Network egress is the main cost driver. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### Hetzner

German provider with excellent price-performance ratio. Popular among European and privacy-conscious developers.

- **Free tier:** None
- **Starting price:** €3.79/mo (CX22 — shared Intel)
- **CX22:** 2 vCPU, 4 GB RAM, 40 GB NVMe SSD, 20 TB bandwidth
- **CX32:** €6.80/mo — 4 vCPU, 8 GB RAM, 80 GB NVMe SSD, 20 TB bandwidth
- **CX42:** €16.40/mo — 8 vCPU, 16 GB RAM, 160 GB NVMe SSD, 20 TB bandwidth
- **CX52:** €32.40/mo — 16 vCPU, 32 GB RAM, 320 GB NVMe SSD, 20 TB bandwidth
- **Pricing model:** Hourly billing; monthly cap (you never pay more than the monthly price). Traffic: 20 TB included for EU/US servers; €1.00/TB overage.
- **Add-ons:** Block storage €0.044/GB/mo; backups +20% of instance price; snapshots €0.011/GB/mo
- **Data centers:** Germany, Finland, USA, Singapore (no Brazil)
- **Notes:** Best price-to-performance ratio among traditional VPS providers. Prices exclude VAT. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### HostGator

Brazilian arm of HostGator, focused on shared hosting and VPS for the Brazilian market.

- **Free tier:** None
- **Starting price:** R$ 25,89/mo (promotional, up to 63% off)
- **Plans:**
  - **VPS 2:** 2 cores, 4 GB DDR5 RAM, 100 GB NVMe, unlimited bandwidth
  - **VPS 4:** 4 cores, 8 GB DDR5 RAM, 200 GB NVMe, unlimited bandwidth
  - **VPS 6:** 6 cores, 16 GB DDR5 RAM, 400 GB NVMe, unlimited bandwidth
  - **VPS 8:** 8 cores, 32 GB DDR5 RAM, 500 GB NVMe, unlimited bandwidth
- **Pricing model:** Monthly; installments up to 12x on credit card; 30-day money-back guarantee
- **Data centers:** Brazil
- **Notes:** All plans include free SSL, unlimited domains, cPanel. Pricing in BRL avoids exchange rate risk.

---

### Hostinger

Budget-friendly provider with data centers in Brazil. Good balance of price and features.

- **Free tier:** None
- **Starting price:** $4.99/mo (promotional; renews higher) — same price across all data center locations including Brazil
- **Entry plan (KVM 1):** 1 vCPU, 4 GB RAM, 50 GB NVMe SSD, 4 TB bandwidth
- **KVM 2:** $6.99/mo — 2 vCPU, 8 GB RAM, 100 GB NVMe SSD, 8 TB bandwidth
- **Pricing model:** Monthly or annual (discount for longer terms); price increases significantly at renewal
- **Data centers:** Brazil, France, India, Lithuania, Netherlands, Singapore, UK, USA
- **Notes:** Weekly automatic backups included free. Includes AI assistant (Kodee). Good entry option for Brazil with local data center.

---

### KingHost

Brazilian provider with national infrastructure and Portuguese-only support.

- **Free tier:** None
- **Starting price:** R$ 29/mo
- **Entry plan (VPS 1GB):** 1 vCPU, 1 GB RAM, 50 GB SSD, unlimited bandwidth
- **Larger plans:** up to 12 vCPU, 32 GB RAM, 350 GB SSD (VPS 32GB)
- **Pricing model:** Monthly or quarterly. 7-day refund policy.
- **Data centers:** Brazil
- **Notes:** Unlimited bandwidth is a highlight. Includes snapshot restore. 99.9% SLA. Pricing discounted for first term; renewals are higher.

---

### Locaweb

One of Brazil's oldest and largest hosting companies. Good for applications requiring Brazilian data residency (LGPD compliance).

- **Free tier:** None
- **Starting price:** R$ 15,90/mo
- **Entry plan (Linux):** 1 vCPU, 512 MB RAM, 20 GB SSD, 1 TB bandwidth
- **Pricing model:** Monthly or quarterly
- **Data centers:** Brazil (São Paulo)
- **Notes:** Good for LGPD compliance. Support via phone, email, chat, and WhatsApp in Portuguese. Established local reputation.

---

### Napoleon

Brazilian hosting provider offering VPS (Cloud), dedicated servers, and cPanel/Plesk reseller hosting.

- **Free tier:** None
- **Starting price:** R$ 195,42/mo (USA region VPS)
- **Entry plan (USA):** 2 GB DDR4 RAM, 40 GB NVMe, CPU EPYC 2x 3.5 GHz, 1x dedicated IPv4, 500 Mbps dedicated link, Anti-DDoS
- **Pricing model:** Monthly; 40% discount on triennial (3-year) billing
- **Data centers:** Brazil, USA (servers also in Canada for bare metal)
- **Notes:** Also offers bare metal, cPanel/Plesk reseller, and LiteSpeed-based shared hosting. 24/7 support in Portuguese via chat, WhatsApp, and Telegram. Includes access to Freepik and Envato Elements.

---

### Northflank

Managed cloud platform for containerized workloads, microservices, and databases. Not a traditional VPS.

- **Free tier:** Developer Sandbox — 2 always-on services, 2 databases, 2 cron jobs (not for production)
- **Starting price:** ~$2.70/mo ($0.0038/hr) for smallest compute
- **Compute pricing:** $0.01667/vCPU/hr + $0.00833/GB RAM/hr
- **GPU options:** NVIDIA A100 40GB at $1.42/hr; H100 at $2.74/hr; B200 at $5.87/hr
- **Pricing model:** Per-second billing; no per-minute platform fee
- **Networking:** First 10 GB/month bandwidth free
- **Data centers:** AWS, GCP, Azure (BYOC); no Brazil-specific region
- **Notes:** PaaS/container-focused (not raw VPS). Supports BYOC to bring your own cloud infrastructure. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### Oracle Cloud

One of the most generous free tiers in the industry. The Always Free ARM tier does not expire.

- **Free tier (always free):**
  - **ARM (Ampere A1):** Up to 4 OCPUs + 24 GB RAM across up to 4 instances (`VM.Standard.A1.Flex`); 200 GB storage total; 10 TB outbound bandwidth/mo
  - **AMD:** 2x `VM.Standard.E2.1.Micro` instances (1/8 OCPU, 1 GB RAM each)
  - Load balancer, object storage (20 GB), VPN, and more included
- **Welcome credit:** $300 for 30 days for new accounts
- **Pricing model:** Pay-as-you-go after free tier; billed per second
- **Data centers:** Multiple regions worldwide (no Brazil region)
- **Notes:** The ARM free tier (4 cores, 24 GB RAM) is the most powerful free cloud offering available. ARM availability can be constrained — retry provisioning during off-peak hours. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### Railway

Developer-friendly PaaS that makes deployment easy without DevOps knowledge. Not a raw VPS.

- **Free tier:** 30-day trial with $5 one-time credit; no ongoing free plan after trial
- **Starting price:** $5/mo (Hobby plan — includes $5 in usage credits)
- **Pro plan:** $20/mo — includes $20 in usage credits; charges delta if usage exceeds plan
- **Pricing model:** Usage-based; charges for actual CPU and memory utilization (idle services cost much less). Credits reset monthly.
- **Data centers:** Multiple regions (no Brazil)
- **Notes:** Best developer experience for simple deployments. Charges for actual utilization, not provisioned resources. Listed as a supported platform in [OpenClaw docs](https://docs.openclaw.ai/vps).

---

### Vultr

Global cloud provider with a data center in São Paulo, Brazil. Wide range of compute options.

- **Free tier:** None (no free trial)
- **Starting price:** $2.50/mo (Regular Cloud Compute — 1 vCPU, 0.5 GB RAM, 10 GB SSD, 0.5 TB bandwidth)
- **Regular Cloud Compute (shared vCPU):** from $2.50/mo — good for low-traffic sites, blogs, dev/test
- **Optimized Cloud Compute (dedicated AMD EPYC/Intel NVMe):** from $6/mo — 1 vCPU, 1 GB RAM, 25 GB NVMe, 2 TB bandwidth
- **VX1 (enterprise, dedicated AMD EPYC):** from ~$112/mo — 4 vCPU, 16 GB RAM, 240 GB NVMe; up to 50 Gbps networking, ~33% cheaper per vCPU than competitors at scale
- **Pricing model:** Hourly billing; VX1 billed on actual hours (not capped at 672); private network traffic within the same DC is free; egress overage $0.01/GB
- **Data centers:** Brazil (São Paulo), Australia, Canada, Germany, France, India, Japan, Netherlands, Singapore, UK, USA, and more (32 locations)
- **Notes:** São Paulo data center makes Vultr a strong option for Brazil-based workloads. VX1 is an enterprise/scale tier, not the starting option.
