def generate_explanation(risks: list):
    if not risks:
        return "No major risks detected in this document."

    lines = []
    for r in risks:
        if r["level"] == "High":
            tone = "⚠️ Important:"
        elif r["level"] == "Medium":
            tone = "ℹ️ Note:"
        else:
            tone = "✔️"

        lines.append(
            f"{tone} {r['explanation']}"
        )

    return " ".join(lines)
