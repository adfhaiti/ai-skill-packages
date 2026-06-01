# Power BI Administration and Security

## Row-Level Security (RLS)

Row-Level Security restricts which data users see based on their identity or role.

### Static RLS (Hardcoded Roles)

Create roles with specific filters:

1. In Desktop, go to Modeling > Create roles
2. Add role (e.g., "Sales Rep Northeast")
3. Select table and add filter: `Region = "Northeast"`
4. Create another role: `Region = "Southeast"`, etc.
5. Test with View as roles before publishing

**DAX Filter Examples**:
```dax
Region = "Northeast"

[SalesRep] = "John Smith"

[Manager] = USERPRINCIPALNAME()

[Date] >= DATE(2024, 1, 1)
```

Limitation: You create each role; good for small, stable groups.

### Dynamic RLS with USERPRINCIPALNAME()

Map user's Azure AD email to data:

1. Create a mapping table with columns: Email, Region, Manager
2. In model, add relationship between mapping table and data table
3. Create RLS role with filter:
   ```dax
   [Email] = USERPRINCIPALNAME()
   ```

Example mapping table:
```
Email                    Region        Manager
john.smith@company.com   Northeast     Mary Johnson
sarah.jones@company.com  Southeast     Tom Williams
```

When Sarah logs in, USERPRINCIPALNAME() returns "sarah.jones@company.com", and she sees only Southeast data.

**Advantages**: Scalable, no role updates needed when staff changes.

### Advanced DAX Patterns

**Manager Hierarchy** (Manager sees own territory plus direct reports):
```dax
OR(
  [SalesRep] = USERPRINCIPALNAME(),
  [Manager] = USERPRINCIPALNAME()
)
```

**Date-Based Access** (See only current and past data):
```dax
[Date] <= TODAY()
```

**Budget Access by Department**:
```dax
[Department] IN VALUES('User Mapping'[Department])
```

**Conditional by Role** (Use LOOKUPVALUE to find role in mapping table):
```dax
VAR UserEmail = USERPRINCIPALNAME()
VAR UserRole = LOOKUPVALUE('User Mapping'[Role], 'User Mapping'[Email], UserEmail)
RETURN
  IF(UserRole = "Executive", TRUE(), [Department] = USERPRINCIPALNAME())
```

### Testing RLS

**In Desktop**:
1. Modeling > View as roles > Select role
2. Report shows data filtered for that role
3. Switch roles to test different views

**In Service** (online):
1. After publishing, go to dataset > Security
2. Test access as specific user
3. Power BI shows what that user would see

**Common Mistakes**:
- Forgetting bidirectional cross-filter on relationship
- RLS on dimension table only (must filter fact table)
- Slow RLS with complex nested functions (test performance)

---

## Workspace Management

Workspaces organize content (reports, dashboards, datasets). Control access by assigning roles.

### Workspace Roles

- **Admin**: Full control, manage access, publish/edit content, delete workspace
- **Member**: Publish/edit content, manage datasets, cannot grant access to new users
- **Contributor**: Edit reports/dashboards, cannot manage workspace or publish datasets
- **Viewer**: View content only, cannot edit

### Dev/Test/Prod Structure

Create three workspaces:

**Dev Workspace**
- For building and testing
- Grant broad access (Contributor/Member)
- Models not optimized, incomplete reports

**Test Workspace**
- Mirror of production setup
- Limit access (Admin, selected testers)
- UAT sign-off here before production

**Prod Workspace**
- Live reports used by business
- Restrict access (Viewer for most, Admin for support)
- Use deployment pipelines for controlled release

### Deployment Pipelines

Power BI Premium feature for safe promotion:

1. Licensing: Premium capacity required
2. Setup: Create pipeline, assign workspaces (Dev, Test, Prod)
3. Deploy: Select content in Dev, click Deploy
4. Power BI moves to Test workspace, test team validates
5. When ready: Deploy from Test to Prod

Benefits:
- Promote multiple reports together
- Deployment history, rollback capability
- Consistent dataset versions across environments

### Power BI Apps

Distribute reports to end users:

1. In workspace, click Create app
2. Select reports/dashboards to include
3. Set app name, description, logo
4. Configure permissions (default is view-only)
5. Publish and share app link

Users:
- See reports in Power BI Service under Apps
- Cannot edit (unless given workspace access)
- Faster, cleaner experience than workspace navigation

---

## Licensing

### License Types

**Free**
- Desktop: Free for individuals
- Service: Limited capacity, shared resources, no refresh scheduling
- Best for: Personal use, trial, learning

**Pro** ($14 USD/month per user)
- Service: Unlimited dashboards/reports in assigned capacity
- Refresh: 8x daily
- Sharing: Can share with other Pro users
- Storage: 10 GB per capacity
- Best for: Collaborative teams, internal BI

**Premium Per User (PPU)** ($24 USD/month per user)
- Service: Premium features (XMLA, paginated reports, AI features)
- Refresh: 48x daily
- No Pro license needed; each user licenses themselves
- Best for: Power users, mixed Pro/PPU teams

**Premium Capacity** (P-SKUs - RETIRING)
- P-SKUs can no longer be purchased new (since July 2024)
- Existing P-SKU renewals ended February 2025
- Full retirement deadline: December 2026
- Organizations must migrate to Fabric F-SKUs before retirement
- All existing P-SKU features are available on equivalent F-SKUs

### Feature Comparison

```
Feature                Free    Pro    PPU    Premium Capacity
Dashboards             Yes     Yes    Yes    Yes
Refresh rate          Manual  8/day  48/day 48/day
Paginated reports      No      No     Yes    Yes
XMLA endpoint          No      No     Yes    Yes
AI visuals             No      No     Yes    Yes
Capacity auto-scale    No      No     No     Yes
Dataflows              Yes     Yes    Yes    Yes
Deployment pipelines   No      No     No     Yes
```

### When Premium is Needed

- Paginated reports (operational, pixel-perfect)
- XMLA endpoint (external tools, Tabular Editor, etc.)
- Large datasets (>1 GB, requires capacity)
- AI features (Q&A, Smart Narrative with training)
- Automation needs (scheduled exports, REST API heavy usage)
- Cost: Premium often cheaper than many Pro licenses if supporting 50+ users

---

## Tenant Administration

Power BI Admin Portal (app.powerbi.com > Admin Portal) controls tenant-wide settings.

### Key Admin Settings

**Tenant Settings**:
- Export to PDF/PowerPoint: Allow or block
- Publish to web: Control public report sharing
- Email subscriptions: Enable/disable
- Service principals: Allow for automation
- Data loss prevention (DLP): Encrypt certain visuals

**Capacity Settings**:
- Monitor usage, set up alerts
- Assign workspaces to capacity
- Configure premium features (XMLA, auto-scale)

**Usage Metrics**:
- Admin > Usage metrics to see adoption
- Dashboard usage, refresh failures, slow queries
- Identify underutilized or overloaded capacity

### Audit Logs

Track all activities (publish, share, delete, access):

1. Admin Portal > Audit logs
2. Search by user, date, activity
3. Export for compliance/troubleshooting

Example: User A shared a sensitive report with the entire organization (audit log shows this, admin can revoke).

### Custom Branding

- Org logo, colors
- Help URL, support portal
- Sign-out text

Found in Admin Portal > Tenant settings > Branding.

---

## On-Premises Data Gateway

Bridges cloud (Power BI) to on-premises data (SQL Server, Oracle, file shares).

### Standard vs. Personal Mode

**Personal Mode**
- Single user, single machine
- Auto-installed with Power BI Desktop (File > Options > Data > Gateway)
- Simple, no setup
- Limitation: Only you can use it; goes offline if your machine shuts down

**Standard Mode**
- Shared, multi-user, dedicated server
- Managed by admin
- Requires Azure AD service account
- Always running, redundant (clustering)

### Installation and Configuration

1. Download from Microsoft Download Center
2. Install on on-premises server
3. Sign in with Azure AD account (service account)
4. Cloud > Cloud settings, add data source connection:
   - Type: SQL Server, Oracle, etc.
   - Server, database, credentials
5. In Power BI Desktop: Get Data > (gateway shows as option)
6. Select gateway and source

### Gateway Clustering

High availability with multiple gateways:

1. Install gateway on multiple servers
2. Same service account on all
3. During install, option to add to existing cluster
4. One becomes primary, others failover
5. If primary fails, traffic routes to next gateway

**Benefits**: No single point of failure, load distribution.

### Monitoring

In Power BI Service, after configuring gateway:
- Settings > Gateways > View refresh history
- See last refresh status, any errors
- Common issues: Timeout (increase timeout in gateway config), credential mismatch

---

## Security Best Practices

### Azure AD Integration

All Power BI users must have Azure AD accounts. Set up:

1. **Single Sign-On (SSO)**: User signs into Windows/Azure AD once
2. **Conditional Access**: Require MFA, block high-risk logins
3. **Provisioning**: Auto-provision users from directory to Power BI

**Conditional Access Policy Example**:
- Require MFA for Power BI access from mobile
- Block access from unmanaged devices
- Limit access to corporate network

### Sensitivity Labels

Classify reports/datasets by sensitivity:

1. In Power BI Service, select report > Info
2. Choose sensitivity label (Public, Internal, Confidential, Restricted)
3. Label applies metadata (shown to users)
4. Can block sharing, prevent download based on label

### Data Loss Prevention (DLP)

Block certain visuals/data from leaving organization:

- Example: Block export of Salary column to CSV
- Prevent copy/paste of PII
- Audit all access

Set in Admin Portal > Tenant settings > Information protection.

### Certified Datasets

Mark trusted datasets as "certified":

1. Dataset owner > Settings > Endorsement
2. Select "Certified" (requires admin approval)
3. Users see certified badge, trust data quality
4. Good for: Published datasets used across reports

**Advantage**: Prevents duplicate/conflicting datasets, ensures single source of truth.

---

## Power BI REST APIs

Automate common tasks with REST APIs.

### Authentication

Most APIs require service principal (app-based auth, not user-based):

1. Register app in Azure AD
2. Grant permissions: Power BI API, Dataset.ReadWrite.All, etc.
3. Get Client ID, Client Secret, Tenant ID
4. Exchange for access token:
   ```
   POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
   client_id={id}&client_secret={secret}&grant_type=client_credentials
   ```
5. Use token in API calls: `Authorization: Bearer {token}`

### Common Automation Scenarios

**Refresh Dataset**:
```
POST https://api.powerbi.com/v1.0/myorg/groups/{workspace}/datasets/{dataset}/refreshes
```

**Export Report to PDF**:
```
POST https://api.powerbi.com/v1.0/myorg/groups/{workspace}/reports/{report}/ExportTo
body: {"format": "PDF"}
```

**Get Dataset Parameters**:
```
GET https://api.powerbi.com/v1.0/myorg/groups/{workspace}/datasets/{dataset}/parameters
```

**Create Workspace**:
```
POST https://api.powerbi.com/v1.0/myorg/groups
body: {"name": "New Workspace"}
```

### Use Cases

- Scheduled exports (nightly report PDF to email)
- Parameter updates (change date range before refresh)
- Workspace automation (create/archive workspaces)
- Usage monitoring (pull refresh stats, performance data)

---

## Version Control and CI/CD

### PBIP Format for Git

Power BI now supports source control via PBIP (Power BI Project) format:

1. File > Save as > Select folder for .pbip format
2. Creates folder with JSON/metadata files (not binary .pbix)
3. Commit to Git: `git add . && git commit -m "Update dashboard"`
4. Share repo with team

**Advantages**:
- Merge conflicts visible (JSON diffs)
- Track all changes (who changed what, when)
- Revert to previous versions easily
- Collaboration without overwriting

### Azure DevOps Workflow

1. Developer clones repo with .pbip file
2. Opens in Power BI Desktop, makes changes, saves
3. Commits: `git commit -m "Add sales trend visual"`
4. Push to feature branch
5. Pull request review (colleague reviews changes in Azure DevOps)
6. Upon approval, merge to main branch
7. Build pipeline runs tests (semantic model validation)
8. Release pipeline deploys to Test workspace
9. Manual approval, then deploy to Prod

### GitHub Actions Workflow

Similar to Azure DevOps, using GitHub Actions:

```yaml
name: Deploy Power BI
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Refresh dataset
        run: |
          curl -X POST https://api.powerbi.com/.../refresh \
            -H "Authorization: Bearer ${{ secrets.PBI_TOKEN }}"
```

### Deployment Pipelines

Built-in Power BI tool for safe promotion:

- Dev workspace: Build and test
- Test workspace: UAT, stakeholder approval
- Prod workspace: Live data
- One-click promote with validation

Better than manual copy-paste between workspaces.

---

## Microsoft Fabric and Copilot Configuration

### Enabling Fabric Capacity

Fabric is Microsoft's unified analytics platform that includes Power BI, Data Factory, Synapse, and more. To enable it:

1. **Prerequisites**: You need either a Fabric capacity (F SKU) or a Power BI Premium capacity (P SKU). Fabric trial is available for individual evaluation.
2. **Enable at tenant level**:
   - Go to **Admin Portal > Tenant settings > Microsoft Fabric**
   - Find **"Users can create Fabric items"** and toggle to Enabled
   - Choose "The entire organization" or limit to specific security groups
   - Click **Apply**
3. **Assign capacity to workspace**:
   - Open the workspace in Power BI Service
   - Click **Settings (gear icon) > Premium**
   - Under "License mode," select **Fabric** or **Premium capacity**
   - Choose the capacity from the dropdown
   - Save
4. **Verify**: Create a new item in the workspace. If Fabric is active, you'll see Fabric item types (Lakehouse, Warehouse, Notebook, etc.) in the **+ New** menu.

**Fabric Trial**: Users can start a 60-day trial from the Power BI Service. Click the account icon (top right) > **Start trial**. This provisions a trial capacity (equivalent to F64).

### Enabling Copilot for Power BI

Copilot requires Fabric capacity (F2 or higher). Steps:

1. **Confirm capacity**: Copilot only works on F2+ capacities (as of April 2025). Previously required F64, but Microsoft lowered the minimum. Shared capacity (Pro/PPU) does not support Copilot.
2. **Enable at tenant level**:
   - Go to **Admin Portal > Tenant settings**
   - Search for **"Copilot"** or navigate to **Microsoft Fabric > Copilot and Azure OpenAI Service**
   - Toggle **"Users can use Copilot and other features powered by Azure OpenAI"** to Enabled
   - Optionally restrict to specific security groups
   - Toggle **"Data sent to Azure OpenAI can be processed outside your capacity's geographic region"** based on your compliance requirements
   - Click **Apply**
3. **Wait for propagation**: Settings can take up to 15 minutes to take effect across the tenant

**Note (September 2025+)**: Copilot is enabled by default for all tenants with eligible capacity. If your tenant was provisioned after September 2025, Copilot is already on. You only need the steps above if it was previously disabled or if you want to restrict it to specific security groups.

4. **Use in Desktop**: Open a report in Power BI Desktop connected to a Fabric-enabled workspace. The Copilot button appears in the ribbon (Home tab)
5. **Use in Service**: Open a report in the Service. Click the Copilot icon in the toolbar

**Common issue**: Copilot button doesn't appear. Check: (a) workspace is assigned to F2+ capacity, (b) tenant setting is enabled, (c) user is in the allowed security group, (d) you waited 15 minutes after enabling.

**Q&A Visual Deprecation**: The standalone Q&A visual is officially deprecated and will be retired in December 2026. Copilot replaces its natural-language query functionality with richer capabilities. Migrate any existing Q&A visuals to Copilot before the retirement deadline.

---

## Power BI Desktop Settings

Key settings that affect model behavior and performance. All accessed via **File > Options and settings > Options**.

### Data Load Settings
**Path**: Options > Current File > Data Load (or Global > Data Load)

- **Auto date/time**: Disabled is recommended for production models. When enabled, Power BI creates hidden date tables for every date column, bloating your model. Path: Data Load > Time Intelligence > uncheck "Auto date/time"
- **Relationships**: "Import relationships from data sources" is useful for SQL databases with FK constraints. "Autodetect new relationships" can be left on during development, but review what it creates.
- **Background data**: "Allow data preview to download in the background" keeps PQ responsive but uses memory.

### Power Query Settings
**Path**: Options > Current File > Power Query (or Global > Power Query)

- **Query folding indicators**: Query folding indicators are available in Power Query Online (Dataflows, Fabric) only. They are NOT available in Power BI Desktop's Power Query Editor as of April 2026. In Desktop, right-click a step and select "View Native Query" to check if a step folds.
- **Query evaluation**: "Enable parallel loading of tables" speeds up refresh when tables are independent.

### Security Settings
**Path**: Options > Global > Security

- **Native database queries**: Controls whether Power Query can run native SQL. Required for custom SQL connections and query folding.
- **R/Python scripting**: Must be enabled to use R or Python visuals.

### Report Settings
**Path**: Options > Current File > Report settings

- **Default visual interactions**: Choose between cross-highlight (default) and cross-filter
- **Persistent filters**: When enabled, report remembers user's filter selections between sessions

### Preview Features
**Path**: Options > Global > Preview features

- New features appear here before general availability
- Enable selectively for testing; don't enable all on production files

---

## Licensing Deep Dive

### License Comparison

| Capability | Free | Pro ($14/user/mo) | PPU ($24/user/mo) | Premium (P1: ~$5K/mo) | Fabric (F2: ~$263/mo+) |
|---|---|---|---|---|---|
| Create reports | Yes | Yes | Yes | Yes | Yes |
| Share with others | No | Pro-to-Pro only | PPU-to-PPU only | Anyone with Free+ | Anyone with Free+ |
| Max dataset size | 1 GB | 1 GB | 100 GB | 400 GB | Varies by SKU |
| Refresh frequency | 8x/day | 8x/day | 48x/day | 48x/day | Varies |
| Paginated reports | No | No | Yes | Yes | Yes |
| Deployment pipelines | No | No | Yes | Yes | Yes |
| XMLA endpoint | No | No | Read-only | Read/Write | Read/Write |
| Dataflows Gen2 | No | Limited | Yes | Yes | Yes |
| Copilot | No | No | No | Yes (P1+, retiring Dec 2026) | Yes (F2+, since Apr 2025) |
| AI visuals | No | No | Yes | Yes | Yes |

### Common Licensing Questions

**"My team can't see my report"**: The report is in a Pro workspace and the viewer has a Free license. Solutions: (a) give them Pro licenses, (b) publish to a Premium/Fabric capacity workspace, or (c) use "Publish to web" if the data is public.

**"Do I need Premium?"**: You need Premium or Fabric if: datasets exceed 1 GB, you need paginated reports, you need more than 8 refreshes/day, you want XMLA endpoint for Tabular Editor, or you want to share with Free users without giving them Pro.

**"What's the difference between PPU and Premium?"**: PPU is per-user and only shareable with other PPU users. Premium is capacity-based and shareable with anyone (even Free users). For small teams (under 25 users), PPU is cheaper. For larger teams or external sharing, Premium/Fabric makes more sense.

---

## Web Sharing and Publishing Settings

### Publish to Web (Public Embedding)
**Path**: Admin Portal > Tenant settings > Export and sharing settings > Publish to web

- **Risk**: This creates a publicly accessible URL. Anyone with the link can see the data. No authentication required.
- **When to use**: Only for publicly available data (e.g., a public dashboard on your organization's website)
- **Enable/Disable**: Admin Portal > Tenant settings > "Publish to web" > toggle and restrict to security groups
- **Managing existing embeds**: Admin Portal > Embed codes > view, revoke, or audit existing public embeds

### External Sharing (B2B)
**Path**: Admin Portal > Tenant settings > Export and sharing settings

- **"Allow Azure Active Directory guest users to access Power BI"**: Enable for external collaborators
- **"Invite external users to your organization"**: Controls who can send B2B invitations
- **"Allow external users to edit and manage content"**: Grants edit (not just view) permission

### Export Controls
**Path**: Admin Portal > Tenant settings > Export and sharing settings

- **Export to Excel**: Toggle per security group. Be cautious with sensitive data.
- **Export to CSV**: Similar controls
- **Export to PDF/PowerPoint**: Toggle per group
- **Print dashboards and reports**: Toggle per group
- **Copy and paste visuals**: Controls whether users can copy visual data

### Embedding in Applications
- **Embed for your organization**: Uses Power BI authentication. Users need Pro/PPU/Premium access.
- **Embed for your customers**: Uses app-owns-data pattern with service principal. Users don't need Power BI licenses. Requires Embedded capacity (A/EM SKU) or Fabric F SKU.

---

## Summary: Security Checklist

Before going live:

- [ ] RLS configured and tested
- [ ] Sensitive data not in visuals without classification
- [ ] Gateway monitoring enabled if on-premises data
- [ ] Audit logs enabled, reviewed weekly
- [ ] Backups: Export .pbix files periodically
- [ ] Workspace structure: Dev/Test/Prod separation
- [ ] Licensing: Correct tier for team size
- [ ] API security: Service principal has minimal permissions
- [ ] DLP policies set for PII columns
- [ ] Users have Azure AD accounts, not personal email
- [ ] MFA enabled for admin accounts
- [ ] Documentation: Who has access, how to request access
