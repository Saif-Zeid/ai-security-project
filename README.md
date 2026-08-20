# Email Phishing Detection Analyzer

A Python cybersecurity project that parses email files and applies explainable, rule-based detection logic to identify common phishing indicators. The analyzer assigns each message a risk score, classifies it as **LOW**, **MEDIUM**, or **HIGH** risk, and explains the evidence behind its decision.

> **Project status:** Active development. The current version is a rule-based detection foundation that can later support machine-learning or AI-assisted analysis.

## Why I Built This

Phishing remains a common entry point for account compromise and malware. I built this project to practice analyzing the same email components a security analyst would review during an investigation: message content, sender information, reply paths, and embedded URLs.

A major design goal was **explainability**. Instead of returning only a label, the program lists the indicators that affected the score so a user or analyst can understand why an email was flagged.

## Current Features

- Parses standard `.eml` files with Python's email library.
- Extracts the sender, recipient, subject, Reply-To, Return-Path, and plain-text body.
- Supports both single-part and multipart messages.
- Detects urgency and social-engineering phrases such as `urgent`, `verify`, and `unusual activity`.
- Compares the sender domain with the Reply-To domain to identify mismatches.
- Extracts HTTP and HTTPS links from the email body.
- Flags links that use a raw IP address instead of a domain name.
- Examines URL domains for suspicious terms such as `login`, `verify`, `secure`, `account`, `update`, and `support`.
- Produces a numerical score, a risk level, and human-readable reasons.
- Includes safe, simulated legitimate and phishing emails for testing.

## How It Works

1. **Parse:** `src/email_parser.py` reads an `.eml` file and converts important headers and body content into structured data.
2. **Analyze:** `src/detector.py` checks the content, sender metadata, and URLs for phishing indicators.
3. **Score:** Each indicator adds a weighted value to the total score.
4. **Explain:** The detector returns the risk level and a list of the exact indicators it found.
5. **Display:** `src/main.py` prints a readable summary of the analysis.

### Current Scoring Model

| Indicator | Score |
|---|---:|
| Each urgency or suspicious phrase | +1 |
| Sender and Reply-To domains do not match | +2 |
| URL uses an IP address instead of a domain | +3 |
| Each suspicious term found in a URL domain | +1 |

| Total score | Risk level |
|---:|---|
| 0–1 | LOW |
| 2–4 | MEDIUM |
| 5+ | HIGH |

The scoring thresholds are currently heuristic and intended for lab testing rather than production use.

## Project Structure

```text
ai-security-project/
├── data/
│   ├── test_legitimate.eml
│   └── test_phishing.eml
├── src/
│   ├── detector.py
│   ├── email_parser.py
│   └── main.py
└── tests/
```

## Environment

- Ubuntu Server 24.04 LTS
- Python 3.12
- Python virtual environment
- Git and GitHub for version control

## Run the Analyzer

From the project root:

```bash
python src/main.py
```

The test file is currently selected in `src/main.py`. Change the path passed to `parse_email()` to analyze a different `.eml` sample.

Example output:

```text
======= PHISHING ANALYSIS =======
Risk: HIGH
Score: 8

Reasons:
- Urgency/suspicious phrase detected: 'urgent'
- Reply-To domain differs from sender domain
- URL detected
- Suspicious word found in domain: 'verify'
- Suspicious word found in domain: 'account'
```

## Skills Demonstrated

- Python programming and modular code organization
- Email header and body analysis
- Phishing and social-engineering detection
- Sender and domain comparison
- URL extraction and parsing
- Risk scoring and explainable security findings
- Safe creation of simulated test data
- Linux development and Git/GitHub version control

## Planned Improvements

- Add automated unit tests for legitimate and phishing samples.
- Accept a file path as a command-line argument.
- Analyze HTML email bodies and link text mismatches.
- Validate IP addresses and normalize URL punctuation.
- Add SPF, DKIM, and DMARC authentication-result analysis.
- Compare visible brand names with sender and link domains.
- Export results as JSON for SIEM or dashboard integration.
- Evaluate machine-learning or AI-assisted classification after establishing a reliable rule-based baseline.

## Ethical Use

All phishing samples in this repository are simulated and intended only for defensive cybersecurity education and testing.
