def detect_phishing(email_data):
    score = 0
    reasons = []

    subject = email_data.get("subject", "").lower()
    body = email_data.get("body", "").lower()
    sender = email_data.get("from", "").lower()
    reply_to = email_data.get("reply_to", "").lower()

    # Check for urgency language
    urgency_words = [
        "urgent",
        "immediately",
        "as soon as possible",
        "verify",
        "suspended",
        "unusual activity"
    ]

    for word in urgency_words:
        if word in subject or word in body:
            score += 1
            reasons.append(f"Urgency/suspicious phrase detected: '{word}'")

    # Check whether Reply-To looks different from sender
    if reply_to and reply_to not in sender:
        score += 2
        reasons.append("Reply-To address differs from sender address")

    # Determine risk level
    if score >= 5:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "score": score,
        "risk": risk,
        "reasons": reasons
    }
