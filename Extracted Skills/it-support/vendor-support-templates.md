# Vendor Support Communication Templates

Ready-to-customize templates for communicating with vendor support teams. All templates follow the structure: context, evidence of what's been tried, specific technical details, and explicit asks.

## Template 1: Microsoft Support (Azure / M365)

**Use for:** Azure subscription issues, grant provisioning, billing disputes, Entra ID escalations, licensing problems.

```
Subject: [Case #XXXXXXXX] - [One-line description of issue]

Hi [Agent Name],

I've completed the troubleshooting steps you provided. Here are the results and the information you requested:

**Steps completed:**
- [Step 1 and result]
- [Step 2 and result]
- [Step 3 and result]

**Requested information:**

1. **Subscription ID:** [ID or "No subscription was provisioned"]
2. **Tenant ID:** [GUID from Entra Admin Center > Overview]
3. **Account used:** [UPN, e.g., josiah@adfayiti.org]
4. **Role:** [Owner / Global Admin / etc.]

**The core issue:** [2-3 sentence summary of what's wrong, stated as facts]

**I need:**
1. [Specific outcome #1]
2. [Specific outcome #2]

Thank you,
[Name]
ADF Haiti
josiah@adfayiti.org
```

**Escalation triggers:**
- No response within 48 hours: call directly using the phone number on the case
- Generic scripted response that doesn't address the issue: reply requesting escalation to Tier 2
- Issue involves billing/charges: explicitly request credit and reference the charge amount and date

## Template 2: Microsoft Support (Feature/Configuration Issue)

**Use for:** Entra ID policy issues, Teams/Exchange configuration, licensing feature access problems.

```
Subject: [Case #XXXXXXXX] - [Feature] not working for [scope]

Hi [Agent Name],

**Environment:**
- Tenant: ADF Haiti (adfayiti.org)
- Affected users: [count and scope]
- Affected applications: [list]
- Licensing: [Microsoft 365 plan]

**Symptoms:**
[Describe what users see, including exact error messages and error codes]

**Diagnostic data:**
- Sign-in logs show: [error code, conditional access status]
- [X] users affected over [timeframe]
- First occurrence: [date]

**Steps already taken:**
1. [Step and result]
2. [Step and result]

**What I need:**
[Specific ask]

Thank you,
[Name]
```

## Template 3: Ubiquiti Community Forum Post

**Use for:** UniFi firmware issues, configuration questions, feature requests. Note: Ubiquiti has no phone support; community forums are the primary support channel.

```
**Device:** [UDR / UDM-Pro-Max / Switch model / AP model]
**Firmware:** [UniFi OS version] / [Network Application version]
**Topology:** [Brief description, e.g., "UDR > Gargoyle (double NAT) > Starlink"]

**Issue:**
[2-3 sentences describing the problem]

**Steps to reproduce:**
1. [Step]
2. [Step]
3. [Observed result]

**Expected behavior:**
[What should happen]

**Diagnostics:**
- [Relevant log output, truncated]
- [Screenshot description]

**What I've tried:**
- [Fix attempt and result]

**Environment notes:**
Remote deployment in Haiti. Starlink WAN. Limited physical access for troubleshooting. Need solutions that can be applied remotely or with minimal on-site steps.
```

## Template 4: ISP / Starlink Support

**Use for:** Service outages, billing questions, coverage issues.

```
Subject: [Service Issue / Billing Question] - Account [number]

**Account:** [Account number or email]
**Location:** Fond-des-Blancs, Haiti
**Service plan:** [Plan name]

**Issue:**
[Description]

**Diagnostics performed:**
- Starlink app obstruction check: [result]
- Speed test results: [down/up/latency]
- Outage duration: [start time to current or end time]
- Other ISP check: [N/A - Starlink is sole WAN]

**Impact:**
This connection serves [St. Boniface Hospital / ADF Haiti office] and supports [healthcare operations / nonprofit operations]. Extended outages affect [specific operations].

**What I need:**
[Specific ask]
```

## Template 5: Hardware Vendor (Warranty/Return)

**Use for:** Amazon Renewed returns, manufacturer warranty claims, defective unit reports.

```
Subject: [Return/Warranty Claim] - Order #[number]

**Product:** [Make/Model]
**Order date:** [date]
**Order number:** [number]
**Seller:** [Seller name on Amazon / vendor]

**Issue:**
[Description of defect or problem]

**Evidence:**
[Photos attached / diagnostic output]

**Note:** This unit is being deployed to Haiti for nonprofit operations. I need resolution within [X days] before the unit ships internationally, after which returns become impractical.

**Requested resolution:**
[ ] Replacement unit
[ ] Refund
[ ] Repair

Thank you,
[Name]
```

## General Communication Principles

1. **Lead with facts, not frustration.** Support agents respond better to organized technical detail than emotional appeals.
2. **Include everything they need in the first message.** Every back-and-forth adds 24-48 hours. Front-load all diagnostic data, screenshots, and account details.
3. **State explicit asks.** "Please provision the subscription" is actionable. "Please help" is not.
4. **Set escalation timelines.** "If I don't hear back by [date], I will call to escalate."
5. **Document case numbers.** Keep a running log of case numbers, agent names, and dates for reference during escalation.
6. **Screenshot everything.** Portal states change. A screenshot taken today proves what the portal showed today.
