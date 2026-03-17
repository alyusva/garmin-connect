# GitHub Configuration

Configuration files for GitHub Actions, issue templates, and PR templates.

## Workflows

### 🔒 Security Check (`security-check.yml`)

**Runs on:** Every push to main/develop and pull requests

**Checks:**
- ✅ No hardcoded credentials (emails, passwords) in code
- ✅ No sensitive files (.env, tokens.json) in repository
- ✅ .gitignore is properly configured
- ✅ Tokens are stored in `/tmp` (not in project)
- ✅ Dependency vulnerabilities scan (Safety)
- ✅ Security linting (Bandit)
- ✅ Code quality checks

**Status Badges:**

Add to your README:
```markdown
[![Security Check](https://github.com/alyusva/garmin-connect/workflows/Security%20Check/badge.svg)](https://github.com/alyusva/garmin-connect/actions)
```

## Security Best Practices

This project follows security best practices:

1. **No credentials in code**: All credentials passed as arguments
2. **Temporary token storage**: Tokens in `/tmp` (cleared on reboot)
3. **Minimal permissions**: OAuth tokens with read-only access
4. **Regular audits**: Automated security scans on every commit
5. **Open source**: Code is transparent and auditable

## Contributing

When contributing, ensure:
- No credentials in commits
- Tests pass
- Security checks pass
- Documentation is updated

---

**Last updated:** March 2026
