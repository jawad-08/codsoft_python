import re
from email_validator import validate_email, EmailNotValidError

def is_valid_phone(phone: str) -> bool:
    return bool(re.fullmatch(r"\d{7,15}", phone))  # 7–15 digits

def is_valid_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
