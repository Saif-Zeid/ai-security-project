from email import policy
from email.parser import BytesParser


def parse_email(file_path):
    """
    Reads an .eml email file and extracts important information.
    """

    with open(file_path, "rb") as email_file:
        message = BytesParser(policy=policy.default).parse(email_file)

    email_data = {
        "from": message.get("From"),
        "to": message.get("To"),
        "subject": message.get("Subject"),
        "reply_to": message.get("Reply-To"),
        "return_path": message.get("Return-Path"),
        "body": ""
    }

    # Extract the text portion of the email
    if message.is_multipart():
        for part in message.walk():

            if part.get_content_type() == "text/plain":
                try:
                    email_data["body"] += part.get_content()
                except Exception:
                    pass
    else:
        try:
            email_data["body"] = message.get_content()
        except Exception:
            pass

    return email_data
