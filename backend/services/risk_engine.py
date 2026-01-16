def analyze_risks(text: str):
    risks = []

    patterns = [
        {
            "keyword": "terminate at any time",
            "level": "High",
            "reason": "One party can end the agreement without notice, which creates power imbalance."
        },
        {
            "keyword": "no liability",
            "level": "High",
            "reason": "You may not be able to claim damages even if harm occurs."
        },
        {
            "keyword": "data may be shared",
            "level": "Medium",
            "reason": "Your personal information could be shared with third parties."
        },
        {
            "keyword": "without notice",
            "level": "Medium",
            "reason": "Actions can be taken without giving you time to respond."
        }
    ]

    lower_text = text.lower()

    for rule in patterns:
        if rule["keyword"] in lower_text:
            risks.append({
                "issue": rule["keyword"],
                "level": rule["level"],
                "explanation": rule["reason"]
            })

    return risks


def calculate_score(risks: list):
    score = 0
    for r in risks:
        if r["level"] == "High":
            score += 3
        elif r["level"] == "Medium":
            score += 2
        else:
            score += 1
    return min(10, score)
