## Incident Summary
Detected multiple failed authentication attempts indicating a potential brute-force attack.

## Detection Method
A Python-based log analysis script identified repeated failed login attempts from a single IP address against the same user account.

## Indicators of Compromise
- Multiple failed login attempts (>5)
- Single source IP
- Successful login following failures

## Severity Assessment
Medium → High (based on successful authentication after failures)

## Recommended Remediation
- Reset affected account credentials
- Block source IP
- Enable MFA
- Review authentication logs for similar patterns
