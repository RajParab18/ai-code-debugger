def analyze_quality(code):
    issues = []
    score = 100

    if "=" in code and " = " not in code:
        issues.append("Add spaces around '='")
        score -= 5

    return score, issues


def code_insights(code):

    insights = []

    if "for" in code:
        insights.append("Loop detected.")

    if "if" in code:
        insights.append("Conditional logic used.")

    if "print" in code or "cout" in code:
        insights.append("Output statement detected.")

    return insights