"""
Simple entropy-based strength estimator.
"""
import math
from typing import Tuple

SPECIAL_CHARS = set("!@#$%^&*()-_=+[]{};:,.<>?/")

def estimate_entropy(password: str) -> float:
    """
    Rough estimate: if passphrase (spaces or separators), estimate 11 bits/word;
    otherwise compute length * log2(pool_size) where pool_size is inferred.
    """
    # detect passphrase
    if " " in password or "-" in password or "_" in password:
        words = len(password.replace("-", " ").replace("_", " ").split())
        return float(words) * 11.0  # rough estimate for typical wordlists

    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in SPECIAL_CHARS for c in password):
        pool += len(SPECIAL_CHARS)

    if pool <= 0:
        return 0.0
    return len(password) * math.log2(pool)

def strength_label(entropy: float) -> Tuple[str, int]:
    """
    Map entropy to label + numeric score (0-100) for progress bar.
    """
    if entropy < 28:
        return "Very Weak", 20
    if entropy < 36:
        return "Weak", 40
    if entropy < 60:
        return "Reasonable", 60
    if entropy < 128:
        return "Strong", 80
    return "Very Strong", 100
