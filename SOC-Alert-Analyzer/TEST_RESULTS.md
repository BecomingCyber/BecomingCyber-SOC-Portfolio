
# SOC Alert Analyzer: Test Results

## Test Case 001: Severity Change Detection

**Objective:** Verify that the analyzer correctly identifies newly qualifying security alerts.

**Test Data:** Five simulated security alerts.

### Test Procedure

1. Execute the analyzer with ALT-003 set to Low severity.
2. Confirm that two alerts match.
3. Change ALT-003 severity from Low to High.
4. Execute the analyzer again.
5. Verify the terminal output and CSV report.

### Expected Results

- Three matching alerts
- ALT-001, ALT-003, and ALT-005 included
- Malware category total remains four

### Actual Results

- Three matching alerts identified
- All three expected alert IDs exported
- Malware category total remained four
- No runtime errors observed

### Test Result: PASS

### Conclusion

The analyzer correctly updated its filtering and CSV output after a simulated alert severity change.
