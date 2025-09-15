sample_report = """
✅ Completed regression testing on Module X
⚠️ Found 3 critical bugs and 2 minor issues
⏳ Pending test cases on Module Y
"""

def analyze_report(text):
    critical = 0
    minor = 0
    completed = 0
    pending = 0
    
    lines = text.split('\n')
    for line in lines:
        if 'critical' in line.lower():
            critical += 1
        if 'minor' in line.lower() or 'minor issues' in line.lower():
            minor += 1
        if 'completed' in line.lower():
            completed += 1
        if 'pending' in line.lower():
            pending += 1
    
    return {
        'critical_bugs': critical,
        'minor_issues': minor,
        'completed_tests': completed,
        'pending_tests': pending
    }

def generate_summary(data):
    summary = f"Critical bugs: {data['critical_bugs']}\n"
    summary += f"Minor issues: {data['minor_issues']}\n"
    summary += f"Completed tests: {data['completed_tests']}\n"
    summary += f"Pending tests: {data['pending_tests']}\n"
    return summary

def classify_risk(critical_bugs):
    if critical_bugs > 5:
        return "High Risk"
    elif critical_bugs >= 1:
        return "Medium Risk"
    else:
        return "Low Risk"

data = analyze_report(sample_report)
summary = generate_summary(data)
risk_level = classify_risk(data['critical_bugs'])

print(summary)
print(f"Risk Level: {risk_level}")
