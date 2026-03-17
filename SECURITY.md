# 🔒 Security Policy

## Credential Handling

This skill requires Garmin Connect credentials to authenticate and fetch data. Here's how credentials are handled:

### ✅ What We DO

- **Command-line arguments only**: Credentials passed as script arguments (not stored in files)
- **Temporary session tokens**: OAuth tokens saved to `/tmp/garmin_session/tokens`
- **Auto-expiration**: Tokens expire after ~24 hours
- **No permanent storage**: No credentials or tokens in config files or database
- **Clear on restart**: `/tmp` directory cleared on system restart

### ❌ What We DON'T DO

- ❌ Store passwords in plaintext
- ❌ Log credentials to files
- ❌ Send credentials to third parties
- ❌ Share tokens between users
- ❌ Keep credentials in memory longer than necessary

## Session Tokens

Session tokens are stored in `/tmp/garmin_session/tokens` with the following properties:

| Property | Value |
|----------|-------|
| **Location** | `/tmp/garmin_session/tokens` |
| **Format** | OAuth2 tokens (JSON) |
| **Lifetime** | ~24 hours |
| **Permissions** | User-only (600) |
| **Cleared** | On system restart |
| **Contains** | Access tokens, NOT passwords |

### Token Permissions

Tokens provide full access to your Garmin Connect account, including:
- ✅ Read all activity data
- ✅ Read health metrics (sleep, HRV, stress)
- ✅ Read user profile
- ⚠️ Potentially modify data (though this skill only reads)

**Important**: Treat tokens like passwords. Don't share them.

## Best Practices

### For Users

1. **Use strong passwords** for your Garmin account
2. **Enable MFA** (Multi-Factor Authentication) on Garmin Connect
3. **Re-authenticate daily** to minimize token exposure
4. **Don't share tokens** with others
5. **Verify this code** before providing credentials (it's open source!)
6. **Use on trusted systems** only
7. **Clear tokens when done**: `rm -rf /tmp/garmin_session`

### For Developers

1. **Never commit credentials** to version control
2. **Never log credentials** to console or files
3. **Use tokenstore parameter** for all `api.login()` calls
4. **Handle errors gracefully** without exposing credentials
5. **Clear sensitive data** from memory when done
6. **Follow principle of least privilege**
7. **Audit dependencies** for vulnerabilities

## Rate Limiting

Garmin Connect API has rate limits to prevent abuse:

- **Rate limit**: ~100-200 requests per hour (not officially documented)
- **Error**: `GarminConnectTooManyRequestsError`
- **Backoff strategy**: Wait 60 seconds, then retry
- **Prevention**: Cache data when possible, batch requests

## Vulnerability Reporting

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. **Email**: [your-email@example.com] with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (optional)
3. **Expected response time**: 48 hours

We will:
- Acknowledge receipt within 48 hours
- Investigate and confirm the issue
- Develop and test a fix
- Release a patched version
- Credit you (if desired) in the release notes

## Security Checklist

Before using this skill:

- [ ] Verified the source code is from the official repository
- [ ] Reviewed authentication code in `scripts/garmin_auth.py`
- [ ] Enabled MFA on Garmin Connect account
- [ ] Using a trusted system (not public/shared computer)
- [ ] Understand that tokens provide full account access
- [ ] Know how to revoke tokens (re-authenticate or clear `/tmp/garmin_session`)

## Data Privacy

### What Data is Accessed?

This skill accesses:
- ✅ Activity data (runs, rides, swims, etc.)
- ✅ Sleep data
- ✅ Heart rate and HRV data
- ✅ Body composition (weight, BMI, body fat)
- ✅ Training metrics (VO2max, fitness age, race predictions)
- ✅ Device information
- ✅ User profile (name, age, gender for calculations)

### Where Does Data Go?

- **Local only**: All data stays on your computer
- **No cloud sync**: Not uploaded to external services
- **Claude API**: Data may be sent to Claude AI for analysis (check Claude's privacy policy)
- **No analytics**: We don't collect usage statistics

### GDPR Compliance

For EU users:
- **Right to access**: You own all data (it's yours from Garmin)
- **Right to erasure**: Clear tokens and data anytime
- **Right to portability**: Data is in JSON format
- **Right to object**: Don't use the skill if you object

## MFA (Multi-Factor Authentication)

If you have MFA enabled on Garmin:

```bash
# You'll receive a 6-digit code via email/SMS/app
python3 scripts/garmin_auth.py your-email@example.com your-password 123456
```

**Important**: MFA codes expire quickly (usually 5 minutes). Use promptly.

## Revoking Access

To revoke this skill's access to your Garmin account:

### Method 1: Clear Tokens
```bash
rm -rf /tmp/garmin_session
```

Tokens expire in ~24 hours anyway.

### Method 2: Change Password
Change your Garmin password at [https://connect.garmin.com/](https://connect.garmin.com/). This invalidates all active sessions.

### Method 3: Garmin Connected Apps
Visit Garmin Connect Settings → Connected Apps and revoke access (if applicable).

## Audit Log

| Date | Version | Change |
|------|---------|--------|
| 2026-03-17 | 1.0.0 | Initial security policy |

## Compliance

This skill aims to comply with:
- ✅ GDPR (General Data Protection Regulation)
- ✅ CCPA (California Consumer Privacy Act)
- ✅ Garmin Connect Terms of Service
- ✅ OAuth 2.0 best practices

## Dependencies Security

Regular dependency audits:

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Update dependencies
pip install --upgrade garminconnect garth
```

Current dependencies:
- `garminconnect` - Garmin API wrapper
- `garth` - Garmin authentication library

Both are open source and actively maintained.

## Responsible Disclosure

We follow responsible disclosure practices:
1. Report received → Acknowledged (48h)
2. Issue verified → Confirmed (1 week)
3. Fix developed → Tested (1-2 weeks)
4. Patch released → Public disclosure (immediately)
5. Credit given → Release notes

Thank you for helping keep this project secure! 🔒

---

**Last updated**: March 2026
**Version**: 1.0.0
