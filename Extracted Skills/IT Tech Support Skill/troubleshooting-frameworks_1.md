# Troubleshooting Frameworks

Diagnostic decision trees for recurring IT problem categories at ADF Haiti.

## 1. Windows Network/File Sharing Errors

**Common error codes:**
- `0x80070035` (network path not found): Name resolution or SMB configuration failure
- `0x800704f8` (unauthenticated guest access blocked): Windows blocking insecure guest logons
- `0x80004005` (unspecified error): Often SMBv1 disabled or credential mismatch

**Diagnostic sequence:**
1. Verify computer name spelling (watch for l/I confusion in hostnames)
2. Test basic connectivity: `ping <hostname>` and `ping <IP>`
3. Check name resolution: `nslookup <hostname>` or `nbtstat -a <hostname>`
4. Verify SMB is enabled: `Get-SmbServerConfiguration | Select EnableSMB2Protocol`
5. Check firewall: `netsh advfirewall firewall show rule name="File and Printer Sharing*"`
6. Verify sharing settings: Control Panel > Network and Sharing Center > Advanced sharing settings
7. Check credentials: `net use` to list active connections; `cmdkey /list` for stored credentials

**Quick fixes to try first:**
```powershell
ipconfig /release
ipconfig /renew
ipconfig /flushdns
net stop workstation && net start workstation
```

**Guest access fix (if appropriate for environment):**
- Group Policy: Computer Configuration > Administrative Templates > Network > Lanman Workstation > Enable insecure guest logons = Enabled
- Registry: `HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters` > DWORD `AllowInsecureGuestAuth` = 1
- Preferred: configure proper authentication on the share server instead

## 2. Microsoft 365 / Entra ID Authentication Failures

**Symptoms:** Users see "Use a certificate or smart card" as only MFA option; users blocked from Teams/SharePoint/Outlook; error 50074 (Strong Authentication required); error 500192 (no valid certificate detected)

**Root cause pattern:** A Conditional Access policy enforces a custom authentication strength requiring certificate-based auth, but users don't have certificates.

**Diagnostic sequence:**
1. Identify scope: one user, one app, or all users/all apps?
2. Check Entra sign-in logs: **Entra Admin Center > Identity > Monitoring & Health > Sign-in logs**
   - Filter by user and status = Failure
   - Note error code and Conditional Access status
3. Review Conditional Access policies: **Protection > Conditional Access > Policies**
   - List all Enabled policies
   - For each, check Grant controls (especially "Require authentication strength")
4. Review authentication strengths: **Protection > Authentication methods > Authentication strengths**
   - Look for custom strengths requiring only certificate-based auth
5. Review authentication methods: **Protection > Authentication methods > Policies**
   - Verify Microsoft Authenticator is Enabled for All Users
   - Verify FIDO2 security key is Enabled if desired

**Immediate fix:**
1. Set problematic Conditional Access policy to **Report-only** mode (not Off, to preserve audit trail)
2. Wait 5-10 minutes for propagation
3. Test sign-in in private browser window
4. Then fix the policy's authentication strength requirement before re-enabling

**Proper fix:**
- Change the policy to use built-in "Multifactor authentication" strength instead of a custom certificate-only strength
- Enable Microsoft Authenticator and FIDO2 in authentication methods policies
- Test with pilot group before re-enabling policy tenant-wide

## 3. Azure Subscription and Grant Issues

**Common scenarios:**
- Nonprofit grant shows "Claimed" but no subscription appears in portal
- Expired sponsorship silently converts to Pay-As-You-Go
- Resources running on unexpected billing context

**Diagnostic sequence:**
1. Check Subscriptions blade with Global subscription filter set to "All"
2. Check Switch directories for additional directories
3. Check microsoftazuresponsorships.com/Balance for sponsorship status
4. Check nonprofit portal at nonprofit.microsoft.com/en-us/offers/azure for grant status
5. Verify account has Owner role on subscription

**Support case strategy:**
- Always include: old subscription ID, new grant details (claim date, amount, email used), tenant ID, screenshots of all portal pages checked
- Explicitly state what does NOT exist (e.g., "no subscription ID was generated")
- Request specific outcomes (provision the grant as a subscription; credit erroneous charges)
- If no response in 48 hours, call directly; email-only cases move slowly
- Use templates in `vendor-support-templates.md`

## 4. UniFi Network Diagnostics

**WiFi connectivity issues:**
1. Check client signal strength: UniFi Dashboard > Clients > select client > Connection quality
2. Check channel utilization: UniFi Dashboard > WiFi > Channel AI (if available)
3. Check for interference: `sudo iwlist wlan0 scan` (Linux) or WiFi Analyzer app (Android)
4. Check for packet loss: `ping -c 100 <gateway IP>` and count lost packets
5. Check logs: UniFi Dashboard > System Logs > filter by client MAC

**Common fixes:**
- Change WiFi channels: use only 1, 6, or 11 for 2.4GHz; non-DFS channels for 5GHz
- Reduce power levels to Medium (prevents oversaturation in small spaces)
- Disable band steering temporarily to isolate 2.4 vs 5GHz issues
- Update firmware only to proven stable versions (check community forums first)

**WAN/Starlink issues:**
1. Ping test: `ping 1.1.1.1` (Cloudflare) and `ping 8.8.8.8` (Google)
2. Traceroute: `tracert 1.1.1.1` (Windows) or `traceroute 1.1.1.1` (Linux)
3. Look for TTL expired errors (routing loops) or repeated IPs in trace
4. Check Starlink app for obstruction data and outage history
5. Check UDR WAN SLA monitoring (if running UniFi Network 9.2.87+)

**Double NAT considerations:**
- Gargoyle on 192.168.2.x provides bandwidth management
- UDR on 192.168.1.x with DMZ pointing to UDR handles routing
- If connectivity breaks, check both layers independently
- Test from device directly connected to UDR first to isolate Gargoyle layer

## 5. Windows Error Resolution (General)

**Blue screen / BSOD:**
1. Note the stop code (e.g., DRIVER_IRQL_NOT_LESS_OR_EQUAL)
2. Check recent updates: `wmic qfe list brief /format:table`
3. Check event log: Event Viewer > Windows Logs > System > filter by Critical and Error
4. Run memory diagnostic: `mdsched.exe`
5. Run disk check: `chkdsk C: /f /r` (requires restart)
6. Run system file checker: `sfc /scannow`
7. If sfc fails: `DISM /Online /Cleanup-Image /RestoreHealth`

**Application crashes / not responding:**
1. Check Task Manager for resource exhaustion (CPU, RAM, Disk)
2. Check Event Viewer > Application logs for error details
3. Try repair: Settings > Apps > [App] > Modify > Repair
4. Clear app cache/temp files if applicable
5. Reinstall as last resort

**Driver issues:**
1. Device Manager > right-click device > Properties > Driver tab
2. Check driver date and version
3. Try: Update driver > Search automatically
4. If update caused issue: Roll Back Driver
5. For persistent issues: download driver from manufacturer site (not Windows Update)

## 6. Hardware Procurement Evaluation Framework

**For any hardware purchase, evaluate against these Haiti-specific criteria:**

| Criterion | Question |
|---|---|
| Repairability | Can components be replaced? Is RAM soldered or SODIMM? |
| Power tolerance | Universal voltage (100-240V)? Pure sine wave required? |
| Spare availability | Can we buy a second unit as backup within budget? |
| Environmental rating | Operating temp range adequate for Haiti climate (40°C+)? |
| Shipping logistics | Weight/size for hand-carry? Fragile components? |
| Warranty reality | Warranty valid internationally? Usable from Haiti? |
| Local management | Cloud-dependent? Works offline? |
| Total cost of ownership | License fees? Subscription costs? 5-year projection? |

**Laptop-specific checks:**
- RAM: SODIMM (upgradeable) vs soldered (fixed). SODIMM strongly preferred.
- Display: minimum FHD 1920x1080. Reject HD 1366x768.
- Keyboard: verify backlit keyboard is included (not standard on all models, e.g., some E14 Gen 4 variants)
- Battery: renewed laptops ship with degraded batteries. Budget $50-80 for replacement.
- SSD: standard M.2 2280 NVMe preferred (easy upgrade path)

## 7. Copilot and Windows Customization Tool Conflicts

**Symptoms:** Copilot sidebar blank in Office apps; Copilot context menu entries unwanted; features disabled after using debloater tools (O&O ShutUp10++, Winaero Tweaker, etc.)

**Registry locations to check:**
- `HKCU\Software\Policies\Microsoft\Windows\WindowsCopilot` > TurnOffWindowsCopilot
- `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsCopilot` > TurnOffWindowsCopilot
- `HKCU\Software\Microsoft\OneDrive` > EnableShellExtensions (for context menu)

**Group Policy path:**
- User Configuration > Administrative Templates > Windows Components > Windows Copilot

**WebView2 dependency:**
```powershell
winget list Microsoft.EdgeWebView2Runtime
# If missing:
winget install Microsoft.EdgeWebView2Runtime
```

**Office repair:**
Settings > Apps > Microsoft 365 > Modify > Online Repair
