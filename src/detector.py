import re

from urllib.parse import urlparse

from email.utils import parseaddr

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
    sender_email = parseaddr(sender)[1]
    reply_email = parseaddr(reply_to)[1]

    if sender_email and reply_email:
        sender_domain = sender_email.split("@")[-1]
        reply_domain = reply_email.split("@")[-1]

        if sender_domain != reply_domain:
            score += 2
            reasons.append(
                f"Reply-To domain '{reply_domain}' differs from sender domain '{sender_domain}'"
            )

    # Find URLs inside the email body
    urls = re.findall(r'https?://[^\s]+', body)

    for url in urls:
        reasons.append(f"URL detected: {url}")

        # Check if URL uses an IP address instead of a domain name
        if re.search(r'https?://\d{1,3}(?:\.\d{1,3}){3}', url):
            score += 3
            reasons.append("Suspicious URL uses an IP address instead of a domain name")

        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()

        suspicious_domain_words = [
            "login",
            "verify",
            "secure",
            "account",
            "update",
            "support"
        ]

        for word in suspicious_domain_words:
            if word in domain:
                score += 1
                reasons.append(f"Suspicious word found in domain: '{word}'")


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
