# ADF Haiti IT Environment Profile

## Organization

- **Name:** ADF Haiti (Association pour le Développement de Fond-des-Blancs)
- **Type:** Haitian-led nonprofit, 10-12 staff
- **Location:** Fond-des-Blancs, Haiti; operations also touch St. Boniface Hospital
- **Domain:** adfayiti.org
- **IT posture:** Self-managed; no local vendor support; director handles IT administration

## Cloud and Identity

| Component | Details |
|---|---|
| Microsoft 365 tenant | adfayiti.org (nonprofit licensing) |
| Entra ID (Azure AD) | Primary identity provider; Conditional Access policies active |
| Azure subscription | Nonprofit grant ($2,000/yr); watch for expired sponsorship auto-converting to PAYG |
| Exchange Online | Primary email (josiah@adfayiti.org, finance@adfayiti.org, etc.) |
| SharePoint/OneDrive | Document management and file sharing |
| Teams | Internal communication |
| Power BI | Reporting and analytics; Fabric F2 capacity (fabricf2forpbiai, East US) |
| Admin email | josiah@adfayiti.org (Global Admin) |

## Workstations

| Device | OS | Role | Notes |
|---|---|---|---|
| Dell XPS 8950 | Windows 11 Pro | Primary desktop | DDR5 (requires DDR5-4800+ UDIMMs for expansion) |
| Lenovo Yoga 6 | Zorin OS (Ubuntu-based) | Secondary/travel | Linux; Remmina for RDP |
| Xiaomi Poco X7 Pro | Android/HyperOS | Mobile | |
| Fleet ThinkPads | Windows 11 Pro | Staff deployment | L14 Gen 3 preferred (SODIMM slots); avoid soldered RAM models |

## Network Infrastructure

| Component | Details |
|---|---|
| Gateway | Ubiquiti UniFi Dream Router (UDR) |
| Switches | UniFi managed switches |
| Access Points | UniFi APs |
| WAN | Starlink (primary, only) |
| Bandwidth management | Gargoyle router (192.168.2.x) in double-NAT config; UDR on 192.168.1.x with DMZ |
| DNS | Manual: Cloudflare 1.1.1.1 (primary), Google 8.8.8.8 (secondary) |
| Firmware policy | Proven stable releases only; test 30+ days before production; avoid bleeding-edge |
| Recommended UniFi Network App | 9.3.43 or 9.3.45 (stability/features balance) |

## Power Infrastructure

| Component | Requirement |
|---|---|
| UPS | Pure sine wave output; 2-4 hour runtime minimum |
| Generator | Automatic voltage regulation (AVR); 72-hour fuel storage |
| Chargers | All USB-C laptop chargers are universal voltage (100-240V) |
| Budget per site | $5,000-$8,000 for power and cooling infrastructure |

## Key Operational Constraints

1. **Internet is unreliable.** Starlink is the sole WAN. Extended outages are normal. All architecture decisions must account for offline operation.
2. **No local IT support.** Troubleshooting must be doable by a non-specialist following clear written instructions, or remotely by the director.
3. **No local parts.** Hardware must be ordered to a US address, inspected, configured, then shipped or hand-carried to Haiti. Amazon Renewed 90-day return windows are useless once equipment is in-country.
4. **Power quality is poor.** Voltage fluctuations, surges, and multi-hour outages are routine. Every piece of equipment needs surge protection and UPS.
5. **Climate is hostile to electronics.** Ambient temps reach 35-40°C in shade; unventilated rooms exceed 50-60°C. Equipment rooms require air conditioning (not optional).
6. **Budget is constrained.** Nonprofit; every dollar saved on IT can fund mission work. Prefer cost-effective solutions with local management capability over premium cloud-dependent platforms.

## Software Stack

| Category | Tools |
|---|---|
| Email client | Superhuman |
| Package managers | UniGetUI, Winget, Scoop |
| Download managers | Free Download Manager, JDownloader (no piracy tools) |
| Media | PotPlayer, MPC-BE |
| Remote desktop | Remmina (Linux), native RDP (Windows) |
| Automation | Claude Desktop with MCP servers (Windows-MCP, Desktop Commander, PDF Tools) |
| Languages | Python, PowerShell, PHP, Rust/Cargo |
| Data collection | Fulcrum (fulcrumapp.com) |
| Donor CRM | Givebutter |
| Reference sites | iFixit, XDA Forums, Ubiquiti Community, ManualsLib |

## Network Equipment Decision Context

The organization evaluated Cisco Meraki vs Ubiquiti for the hospital network gateway. Decision: **Ubiquiti UniFi (UDM-Pro-Max recommended for hospital; UDR for smaller sites).** Rationale:
- Meraki's cloud dependency is a critical liability with Haiti's unreliable internet
- Ubiquiti's local management works during outages
- 75% cost savings ($1,693 vs $31,285 over 5 years)
- Savings reinvested in power/cooling/spares infrastructure
- Fortinet FortiGate 100F/200F is the middle-ground alternative if Ubiquiti's security history is unacceptable
