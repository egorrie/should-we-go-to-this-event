def score_event(audience_fit, estimated_leads, total_cost, travel, strategic_value):
    score = 0
    reasons = []

    # Audience fit
    if audience_fit == "high":
        score += 3
        reasons.append("strong audience fit")
    elif audience_fit == "medium":
        score += 1
        reasons.append("decent audience fit")
    else:
        reasons.append("weak audience fit")

    # Lead potential
    if estimated_leads >= 50:
        score += 2
        reasons.append("good lead potential")
    elif estimated_leads >= 20:
        score += 1
        reasons.append("some lead potential")
    else:
        reasons.append("limited lead potential")

    # Cost
    if total_cost <= 3000:
        score += 2
        reasons.append("manageable cost")
    elif total_cost <= 7000:
        score += 1
        reasons.append("moderate cost")
    else:
        reasons.append("high cost")

    # Travel
    if travel == "local":
        score += 1
        reasons.append("easy travel")
    elif travel == "regional":
        reasons.append("some travel required")
    else:
        score -= 1
        reasons.append("higher travel burden")

    # Strategic value
    if strategic_value == "high":
        score += 2
        reasons.append("strong strategic value")
    elif strategic_value == "medium":
        score += 1
        reasons.append("some strategic value")
    else:
        reasons.append("limited strategic value")

    return score, reasons


def make_recommendation(score):
    if score >= 8:
        return "Go", "This looks like a strong investment."
    elif score >= 5:
        return "Maybe", "There is some value here, but the ROI is less clear."
    return "Skip", "The tradeoffs likely outweigh the upside."


def main():
    print("Should We Go to This Event?")
    print("-" * 30)

    audience_fit = input("Audience fit (high / medium / low): ").strip().lower()
    estimated_leads = int(input("Estimated leads: ").strip())
    total_cost = int(input("Total cost in dollars: ").strip())
    travel = input("Travel required (local / regional / long-haul): ").strip().lower()
    strategic_value = input("Strategic value (high / medium / low): ").strip().lower()

    score, reasons = score_event(
        audience_fit=audience_fit,
        estimated_leads=estimated_leads,
        total_cost=total_cost,
        travel=travel,
        strategic_value=strategic_value,
    )

    decision, note = make_recommendation(score)

    print("\nRecommendation:", decision)
    print("Score:", score)
    print("Note:", note)
    print("Why:")
    for reason in reasons:
        print(f"- {reason}")


if __name__ == "__main__":
    main()